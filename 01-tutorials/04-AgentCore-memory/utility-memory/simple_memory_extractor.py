#!/usr/bin/env python3
"""
Simple AgentCore Memory Content Extractor

A focused script to extract and print current values from AgentCore long-term memory.
"""

import logging
from typing import List, Dict, Any
from bedrock_agentcore.memory.client import MemoryClient
from bedrock_agentcore.memory.session import MemorySessionManager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def extract_and_print_memory_contents(memory_id: str, region_name: str = "us-east-1"):
    """
    Extract and print all long-term memory contents from AgentCore.
    
    Args:
        memory_id: The AgentCore memory resource ID
        region_name: AWS region (default: us-east-1)
    """
    try:
        print(f"\n{'='*80}")
        print(f"EXTRACTING AGENTCORE LONG-TERM MEMORY CONTENTS")
        print(f"Memory ID: {memory_id}")
        print(f"Region: {region_name}")
        print(f"{'='*80}")
        
        # Initialize clients
        memory_client = MemoryClient(region_name=region_name)
        session_manager = MemorySessionManager(memory_id=memory_id, region_name=region_name)
        
        # Get memory details and strategies
        print("\n📋 MEMORY CONFIGURATION:")
        print("-" * 50)
        
        memory_details = memory_client.gmcp_client.get_memory(memoryId=memory_id)
        memory = memory_details["memory"]
        
        print(f"Name: {memory.get('name', 'N/A')}")
        print(f"Status: {memory.get('status', 'N/A')}")
        print(f"Description: {memory.get('description', 'N/A')}")
        
        # List strategies and their namespaces
        strategies = memory.get('strategies', [])
        print(f"\nStrategies: {len(strategies)} configured")
        
        all_namespaces = set()
        for i, strategy in enumerate(strategies, 1):
            strategy_name = strategy.get('name', 'Unnamed')
            strategy_type = strategy.get('type', 'Unknown')
            namespaces = strategy.get('namespaces', [])
            
            print(f"  {i}. {strategy_name} ({strategy_type})")
            print(f"     Namespaces: {namespaces}")
            
            # Collect all namespaces
            all_namespaces.update(namespaces)
        
        # First, let's get all actors to resolve namespace templates
        print(f"\n👥 DISCOVERING ACTORS:")
        print("-" * 50)
        
        try:
            actors = session_manager.list_actors()
            print(f"Found {len(actors)} actors:")
            for actor in actors:
                actor_id = actor.get('actorId', 'N/A')
                print(f"  - Actor ID: {actor_id}")
        except Exception as e:
            print(f"❌ Failed to list actors: {e}")
            actors = []
        
        # Extract records from each namespace
        print(f"\n📦 EXTRACTING MEMORY RECORDS:")
        print("-" * 50)
        
        total_records = 0
        
        for namespace_template in sorted(all_namespaces):
            print(f"\n🔍 Namespace Template: {namespace_template}")
            
            # Check if namespace contains template variables
            if '{' in namespace_template:
                print("   Contains template variables - attempting to resolve...")
                
                # Try to resolve with available actors and strategies
                resolved_namespaces = []
                
                if actors:
                    for actor in actors:
                        actor_id = actor.get('actorId')
                        if actor_id:
                            # Try to resolve the template
                            for strategy in strategies:
                                strategy_id = strategy.get('strategyId', strategy.get('memoryStrategyId'))
                                if strategy_id:
                                    try:
                                        resolved_ns = namespace_template.format(
                                            actorId=actor_id,
                                            memoryStrategyId=strategy_id,
                                            sessionId="*"  # Use wildcard for session
                                        )
                                        # Remove the sessionId part if it creates invalid pattern
                                        if '/sessions/*' in resolved_ns:
                                            resolved_ns = resolved_ns.replace('/sessions/*', '')
                                        resolved_namespaces.append(resolved_ns)
                                    except KeyError:
                                        # Template variable not available
                                        continue
                
                # Also try some common resolved patterns
                if not resolved_namespaces:
                    # Try common patterns without template variables
                    base_patterns = [
                        namespace_template.split('/')[0] if '/' in namespace_template else namespace_template,
                        "semantic",
                        "preferences", 
                        "facts",
                        "support"
                    ]
                    resolved_namespaces = [p for p in base_patterns if not '{' in p]
                
                print(f"   Resolved to {len(resolved_namespaces)} concrete namespaces")
                
            else:
                # Namespace is already concrete
                resolved_namespaces = [namespace_template]
            
            # Query each resolved namespace
            for namespace in resolved_namespaces:
                if not namespace or '{' in namespace:
                    continue
                    
                print(f"   Querying: {namespace}")
                
                try:
                    # List all records in this namespace
                    records = session_manager.list_long_term_memory_records(
                        namespace_prefix=namespace,
                        max_results=50
                    )
                    
                    if records:
                        print(f"     ✅ Found {len(records)} records:")
                        
                        for j, record in enumerate(records, 1):
                            record_id = record.get('memoryRecordId', 'N/A')
                            created = record.get('createdAt', 'N/A')
                            
                            # Extract content
                            content = record.get('content', {})
                            text_content = content.get('text', 'No content')
                            
                            # Truncate long content
                            display_text = text_content[:150] + "..." if len(text_content) > 150 else text_content
                            
                            print(f"       {j}. ID: {record_id}")
                            print(f"          Created: {created}")
                            print(f"          Content: {display_text}")
                            print()
                        
                        total_records += len(records)
                    else:
                        print(f"     No records found in {namespace}")
                        
                except Exception as e:
                    print(f"     ❌ Error accessing {namespace}: {e}")
        
        # Try searching with common queries if no records found
        if total_records == 0:
            print(f"\n🔍 NO RECORDS FOUND - TRYING SEMANTIC SEARCH:")
            print("-" * 50)
            
            search_queries = ["user", "customer", "conversation", "interaction", "support"]
            
            # Create a list of concrete namespaces for searching
            search_namespaces = []
            
            # Add resolved namespaces from above
            for namespace_template in all_namespaces:
                if '{' in namespace_template:
                    # Try to create concrete namespaces for search
                    if actors:
                        for actor in actors:
                            actor_id = actor.get('actorId')
                            if actor_id:
                                for strategy in strategies:
                                    strategy_id = strategy.get('strategyId', strategy.get('memoryStrategyId'))
                                    if strategy_id:
                                        try:
                                            resolved_ns = namespace_template.format(
                                                actorId=actor_id,
                                                memoryStrategyId=strategy_id,
                                                sessionId="*"
                                            )
                                            if '/sessions/*' in resolved_ns:
                                                resolved_ns = resolved_ns.replace('/sessions/*', '')
                                            search_namespaces.append(resolved_ns)
                                        except KeyError:
                                            continue
                    
                    # Also try base patterns
                    base_ns = namespace_template.split('/')[0] if '/' in namespace_template else namespace_template
                    if not '{' in base_ns:
                        search_namespaces.append(base_ns)
                else:
                    search_namespaces.append(namespace_template)
            
            # Add some common fallback namespaces
            search_namespaces.extend(["semantic", "preferences", "facts", "support", "customer"])
            
            # Remove duplicates and invalid namespaces
            search_namespaces = list(set([ns for ns in search_namespaces if ns and not '{' in ns]))
            
            print(f"Searching in {len(search_namespaces)} namespaces: {search_namespaces}")
            
            for namespace in search_namespaces:
                for query in search_queries:
                    try:
                        search_results = session_manager.search_long_term_memories(
                            query=query,
                            namespace_prefix=namespace,
                            top_k=5
                        )
                        
                        if search_results:
                            print(f"\n🎯 Found {len(search_results)} records for query '{query}' in {namespace}:")
                            
                            for k, record in enumerate(search_results, 1):
                                content = record.get('content', {}).get('text', 'No content')
                                score = record.get('relevanceScore', 0)
                                display_text = content[:100] + "..." if len(content) > 100 else content
                                
                                print(f"   {k}. Score: {score:.3f}")
                                print(f"      Content: {display_text}")
                            
                            total_records += len(search_results)
                            break  # Found records, move to next namespace
                            
                    except Exception as e:
                        continue
        
        # Summary
        print(f"\n{'='*80}")
        print(f"EXTRACTION SUMMARY")
        print(f"{'='*80}")
        print(f"Total Records Found: {total_records}")
        print(f"Namespaces Searched: {len(all_namespaces)}")
        print(f"Strategies Configured: {len(strategies)}")
        
        if total_records == 0:
            print("\n💡 TIPS:")
            print("- Memory might be empty or still processing")
            print("- Check if events have been stored using create_event()")
            print("- Verify memory strategies are ACTIVE")
            print("- Wait for memory extraction to complete (can take 2-3 minutes)")
        
    except Exception as e:
        logger.error(f"❌ Failed to extract memory contents: {e}")
        raise


def list_available_memories(region_name: str = "us-east-1") -> List[Dict[str, Any]]:
    """
    List all available memory resources in the account.
    
    Args:
        region_name: AWS region
        
    Returns:
        List of memory resources
    """
    try:
        memory_client = MemoryClient(region_name=region_name)
        memories = memory_client.list_memories()
        
        print(f"\n📋 AVAILABLE MEMORIES ({len(memories)}):")
        print("-" * 50)
        
        for i, memory in enumerate(memories, 1):
            memory_id = memory.get('memoryId') or memory.get('id')
            name = memory.get('name', 'Unnamed')
            status = memory.get('status', 'Unknown')
            
            print(f"{i}. Memory ID: {memory_id}")
            print(f"   Name: {name}")
            print(f"   Status: {status}")
            print()
        
        return memories
        
    except Exception as e:
        logger.error(f"❌ Failed to list memories: {e}")
        raise


def main():
    """Main function - modify this to use your specific memory ID."""
    
    # Configuration
    REGION = "us-east-1"  # Change to your region
    MEMORY_ID = None      # Set your memory ID here, or leave None to list available memories
    
    try:
        if MEMORY_ID:
            # Extract from specific memory
            extract_and_print_memory_contents(MEMORY_ID, REGION)
        else:
            # List available memories first
            memories = list_available_memories(REGION)
            
            if memories:
                # Use the first memory found
                first_memory = memories[0]
                memory_id = first_memory.get('memoryId') or first_memory.get('id')
                
                print(f"\n🔍 Using first available memory: {memory_id}")
                extract_and_print_memory_contents(memory_id, REGION)
            else:
                print("❌ No memories found. Create a memory resource first.")
    
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()