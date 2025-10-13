#!/usr/bin/env python3
"""
Fixed AgentCore Memory Content Extractor

This version properly handles namespace template resolution to avoid validation errors.
"""

import logging
from typing import List, Dict, Any
from bedrock_agentcore.memory.client import MemoryClient
from bedrock_agentcore.memory.session import MemorySessionManager

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def resolve_namespace_templates(namespace_templates: List[str], actors: List[Dict], strategies: List[Dict]) -> List[str]:
    """
    Resolve namespace templates with actual actor and strategy IDs.
    
    Args:
        namespace_templates: List of namespace templates with variables
        actors: List of actor objects
        strategies: List of strategy objects
        
    Returns:
        List of concrete namespace strings
    """
    concrete_namespaces = []
    
    for template in namespace_templates:
        if '{' not in template:
            # Already concrete
            concrete_namespaces.append(template)
            continue
            
        # Try to resolve template variables
        resolved = False
        
        if actors:
            for actor in actors:
                actor_id = actor.get('actorId')
                if not actor_id:
                    continue
                    
                for strategy in strategies:
                    strategy_id = strategy.get('strategyId') or strategy.get('memoryStrategyId')
                    if not strategy_id:
                        continue
                        
                    try:
                        # Try to resolve all template variables
                        resolved_ns = template.format(
                            actorId=actor_id,
                            memoryStrategyId=strategy_id,
                            sessionId="*"  # Use wildcard for sessions
                        )
                        
                        # Clean up session wildcards that create invalid patterns
                        if '/sessions/*' in resolved_ns:
                            resolved_ns = resolved_ns.replace('/sessions/*', '')
                        
                        # Validate the resolved namespace doesn't have remaining templates
                        if '{' not in resolved_ns and resolved_ns not in concrete_namespaces:
                            concrete_namespaces.append(resolved_ns)
                            resolved = True
                            
                    except KeyError:
                        # Template has variables we can't resolve
                        continue
        
        # If we couldn't resolve the template, try to extract a base namespace
        if not resolved:
            # Extract the first part before any template variables
            parts = template.split('/')
            base_parts = []
            for part in parts:
                if '{' in part:
                    break
                base_parts.append(part)
            
            if base_parts:
                base_ns = '/'.join(base_parts)
                if base_ns and base_ns not in concrete_namespaces:
                    concrete_namespaces.append(base_ns)
    
    return concrete_namespaces


def extract_and_print_memory_contents(memory_id: str, region_name: str = "us-east-1"):
    """
    Extract and print all long-term memory contents from AgentCore.
    Fixed version that properly handles namespace templates.
    """
    try:
        print(f"\n{'='*80}")
        print(f"EXTRACTING AGENTCORE LONG-TERM MEMORY CONTENTS (FIXED) for memory_id",{memory_id})
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
        
        all_namespace_templates = set()
        for i, strategy in enumerate(strategies, 1):
            strategy_name = strategy.get('name', 'Unnamed')
            strategy_type = strategy.get('type', 'Unknown')
            strategy_status = strategy.get('status', 'Unknown')
            namespaces = strategy.get('namespaces', [])
            
            print(f"  {i}. {strategy_name} ({strategy_type}) - Status: {strategy_status}")
            print(f"     Namespaces: {namespaces}")
            
            # Collect all namespace templates
            all_namespace_templates.update(namespaces)
        
        # Discover actors for namespace resolution
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
        
        # Resolve namespace templates
        print(f"\n🔧 RESOLVING NAMESPACE TEMPLATES:")
        print("-" * 50)
        
        concrete_namespaces = resolve_namespace_templates(
            list(all_namespace_templates), 
            actors, 
            strategies
        )
        
        print(f"Template namespaces: {len(all_namespace_templates)}")
        for template in sorted(all_namespace_templates):
            print(f"  - {template}")
        
        print(f"\nResolved to {len(concrete_namespaces)} concrete namespaces:")
        for namespace in sorted(concrete_namespaces):
            print(f"  - {namespace}")
        
        # Extract records from each concrete namespace
        print(f"\n📦 EXTRACTING MEMORY RECORDS:")
        print("-" * 50)
        
        total_records = 0
        
        for namespace in sorted(concrete_namespaces):
            print(f"\n🔍 Namespace: {namespace}")
            
            try:
                # List all records in this namespace
                records = session_manager.list_long_term_memory_records(
                    namespace_prefix=namespace,
                    max_results=50
                )
                
                if records:
                    print(f"   ✅ Found {len(records)} records:")
                    
                    for j, record in enumerate(records, 1):
                        record_id = record.get('memoryRecordId', 'N/A')
                        created = record.get('createdAt', 'N/A')
                        strategy_id = record.get('memoryStrategyId', 'N/A')
                        
                        # Extract content
                        content = record.get('content', {})
                        text_content = content.get('text', 'No content')
                        
                        # Truncate long content
                        display_text = text_content[:500] + "..." if len(text_content) > 500 else text_content
                        
                        print(f"     {j}. ID: {record_id}")
                        print(f"        Strategy: {strategy_id}")
                        print(f"        Created: {created}")
                        print(f"        Content: {display_text}")
                        print()
                    
                    total_records += len(records)
                else:
                    print("   No records found")
                    
            except Exception as e:
                print(f"   ❌ Error accessing namespace '{namespace}': {e}")
        
        # Try semantic search if no records found
        if total_records == 0:
            print(f"\n🔍 NO RECORDS FOUND - TRYING SEMANTIC SEARCH:")
            print("-" * 50)
            
            search_queries = ["user", "customer", "conversation", "interaction", "support", "travel", "booking"]
            
            for namespace in concrete_namespaces:
                print(f"\nSearching in namespace: {namespace}")
                
                for query in search_queries:
                    try:
                        search_results = session_manager.search_long_term_memories(
                            query=query,
                            namespace_prefix=namespace,
                            top_k=3
                        )
                        
                        if search_results:
                            print(f"  🎯 Query '{query}' found {len(search_results)} results:")
                            
                            for k, record in enumerate(search_results, 1):
                                content = record.get('content', {}).get('text', 'No content')
                                score = record.get('relevanceScore', 0)
                                display_text = content[:300] + "..." if len(content) > 300 else content
                                
                                print(f"    {k}. Score: {score:.3f}")
                                print(f"       Content: {display_text}")
                            
                            total_records += len(search_results)
                            break  # Found results, move to next namespace
                            
                    except Exception as e:
                        continue
                
                if total_records > 0:
                    break  # Found some results, stop searching
        
        # Summary
        print(f"\n{'='*80}")
        print(f"EXTRACTION SUMMARY")
        print(f"{'='*80}")
        print(f"Total Records Found: {total_records}")
        print(f"Concrete Namespaces: {len(concrete_namespaces)}")
        print(f"Template Namespaces: {len(all_namespace_templates)}")
        print(f"Strategies Configured: {len(strategies)}")
        print(f"Actors Found: {len(actors)}")
        
        if total_records == 0:
            print("\n💡 TROUBLESHOOTING:")
            print("- Memory might be empty or still processing")
            print("- Check if events have been stored using create_event() or add_turns()")
            print("- Verify memory strategies are ACTIVE")
            print("- Wait for memory extraction to complete (2-3 minutes after storing events)")
            print("- Check that namespace patterns match your stored data")
        else:
            print(f"\n✅ Successfully extracted {total_records} memory records!")
        
    except Exception as e:
        logger.error(f"❌ Failed to extract memory contents: {e}")
        raise


def main():
    """Main function - modify this to use your specific memory ID."""
    
    # Configuration
    REGION = "us-west-2"  # Change to your region
    # MEMORY_ID = None      # Set your memory ID here, or leave None to list available memories
    MEMORY_ID ="TravelAgent_STM_20251012114311-E9nNWYBpoW"
    
    try:
        if MEMORY_ID:
            # Extract from specific memory
            extract_and_print_memory_contents(MEMORY_ID, REGION)
        else:
            # List available memories first
            memory_client = MemoryClient(region_name=REGION)
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
            
            if memories:
                # Use the first memory found
                first_memory = memories[0]
                memory_id = first_memory.get('memoryId') or first_memory.get('id')
                # memory_id ="TravelAgent_STM_20251012114311-E9nNWYBpoW"
                
                print(f"\n🔍 Using first available memory: {memory_id}")
                extract_and_print_memory_contents(memory_id, REGION)
            else:
                print("❌ No memories found. Create a memory resource first.")
    
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    main()