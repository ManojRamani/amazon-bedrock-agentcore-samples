#!/usr/bin/env python3
"""
Extract and Print AgentCore Long-Term Memory Contents

This script demonstrates how to extract and display the current values stored in 
AWS Bedrock AgentCore long-term memory using the MemoryClient and MemorySessionManager.

Requirements:
- AWS credentials configured
- bedrock-agentcore package installed
- Appropriate IAM permissions for AgentCore Memory operations
"""

import logging
import json
from typing import Dict, List, Optional, Any
from datetime import datetime

# AgentCore Memory imports
from bedrock_agentcore.memory.client import MemoryClient
from bedrock_agentcore.memory.session import MemorySessionManager
from bedrock_agentcore.memory.models import MemoryRecord

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class AgentCoreMemoryExtractor:
    """
    Extracts and displays contents from AgentCore long-term memory.
    
    This class provides methods to:
    - List all available memories
    - Extract memory records from specific namespaces
    - Display memory strategies and configurations
    - Print formatted memory contents
    """
    
    def __init__(self, region_name: str = "us-east-1"):
        """
        Initialize the memory extractor.
        
        Args:
            region_name: AWS region where AgentCore Memory is deployed
        """
        self.region_name = region_name
        self.memory_client = MemoryClient(region_name=region_name)
        logger.info(f"✅ Initialized AgentCore Memory extractor for region: {region_name}")
    
    def list_all_memories(self) -> List[Dict[str, Any]]:
        """
        List all available memory resources in the account.
        
        Returns:
            List of memory resource summaries
        """
        try:
            memories = self.memory_client.list_memories(max_results=100)
            logger.info(f"📋 Found {len(memories)} memory resources")
            return memories
        except Exception as e:
            logger.error(f"❌ Failed to list memories: {e}")
            raise
    
    def get_memory_details(self, memory_id: str) -> Dict[str, Any]:
        """
        Get detailed information about a specific memory resource.
        
        Args:
            memory_id: The memory resource ID
            
        Returns:
            Memory resource details including strategies
        """
        try:
            # Get memory details using the control plane client
            response = self.memory_client.gmcp_client.get_memory(memoryId=memory_id)
            memory = response["memory"]
            
            logger.info(f"📄 Retrieved details for memory: {memory_id}")
            return memory
        except Exception as e:
            logger.error(f"❌ Failed to get memory details: {e}")
            raise
    
    def extract_memory_records(
        self, 
        memory_id: str, 
        namespace_prefix: str = "",
        strategy_id: Optional[str] = None,
        max_results: int = 50
    ) -> List[MemoryRecord]:
        """
        Extract memory records from a specific namespace.
        
        Args:
            memory_id: The memory resource ID
            namespace_prefix: Namespace prefix to filter records (empty for all)
            strategy_id: Optional strategy ID to filter by
            max_results: Maximum number of records to retrieve
            
        Returns:
            List of memory records
        """
        try:
            session_manager = MemorySessionManager(memory_id=memory_id, region_name=self.region_name)
            
            if namespace_prefix:
                # List records from specific namespace
                records = session_manager.list_long_term_memory_records(
                    namespace_prefix=namespace_prefix,
                    strategy_id=strategy_id,
                    max_results=max_results
                )
            else:
                # If no namespace specified, we need to get all namespaces
                # This requires listing by strategy or using a broad search
                records = []
                logger.warning("⚠️  No namespace specified. Use search_memory_records for broader extraction.")
            
            logger.info(f"📦 Extracted {len(records)} memory records from namespace: {namespace_prefix or 'all'}")
            return records
            
        except Exception as e:
            logger.error(f"❌ Failed to extract memory records: {e}")
            raise
    
    def search_memory_records(
        self, 
        memory_id: str, 
        query: str,
        namespace_prefix: str,
        top_k: int = 10
    ) -> List[MemoryRecord]:
        """
        Search memory records using semantic search.
        
        Args:
            memory_id: The memory resource ID
            query: Search query
            namespace_prefix: Namespace to search within
            top_k: Number of top results to return
            
        Returns:
            List of relevant memory records
        """
        try:
            session_manager = MemorySessionManager(memory_id=memory_id, region_name=self.region_name)
            
            records = session_manager.search_long_term_memories(
                query=query,
                namespace_prefix=namespace_prefix,
                top_k=top_k
            )
            
            logger.info(f"🔍 Found {len(records)} records matching query: '{query}'")
            return records
            
        except Exception as e:
            logger.error(f"❌ Failed to search memory records: {e}")
            raise
    
    def print_memory_summary(self, memory_id: str):
        """
        Print a comprehensive summary of a memory resource.
        
        Args:
            memory_id: The memory resource ID
        """
        try:
            print(f"\n{'='*80}")
            print(f"AGENTCORE MEMORY SUMMARY")
            print(f"{'='*80}")
            
            # Get memory details
            memory = self.get_memory_details(memory_id)
            
            print(f"Memory ID: {memory.get('id', 'N/A')}")
            print(f"Name: {memory.get('name', 'N/A')}")
            print(f"Description: {memory.get('description', 'N/A')}")
            print(f"Status: {memory.get('status', 'N/A')}")
            print(f"Created: {memory.get('createdAt', 'N/A')}")
            print(f"Updated: {memory.get('updatedAt', 'N/A')}")
            print(f"Event Expiry: {memory.get('eventExpiryDuration', 'N/A')} days")
            
            # Print strategies
            strategies = memory.get('strategies', [])
            print(f"\n📋 MEMORY STRATEGIES ({len(strategies)} configured):")
            print("-" * 60)
            
            for i, strategy in enumerate(strategies, 1):
                print(f"{i}. Strategy ID: {strategy.get('strategyId', 'N/A')}")
                print(f"   Name: {strategy.get('name', 'N/A')}")
                print(f"   Type: {strategy.get('type', 'N/A')}")
                print(f"   Status: {strategy.get('status', 'N/A')}")
                print(f"   Description: {strategy.get('description', 'N/A')}")
                
                # Print namespaces
                namespaces = strategy.get('namespaces', [])
                if namespaces:
                    print(f"   Namespaces: {', '.join(namespaces)}")
                print()
            
        except Exception as e:
            logger.error(f"❌ Failed to print memory summary: {e}")
            raise
    
    def print_memory_records(self, records: List[MemoryRecord], title: str = "MEMORY RECORDS"):
        """
        Print formatted memory records.
        
        Args:
            records: List of memory records to print
            title: Title for the output section
        """
        print(f"\n{'='*80}")
        print(f"{title} ({len(records)} records)")
        print(f"{'='*80}")
        
        if not records:
            print("No memory records found.")
            return
        
        for i, record in enumerate(records, 1):
            print(f"\n📄 Record {i}:")
            print("-" * 40)
            print(f"Record ID: {record.get('memoryRecordId', 'N/A')}")
            print(f"Strategy ID: {record.get('memoryStrategyId', 'N/A')}")
            print(f"Namespace: {record.get('namespace', 'N/A')}")
            print(f"Created: {record.get('createdAt', 'N/A')}")
            print(f"Updated: {record.get('updatedAt', 'N/A')}")
            
            # Print content
            content = record.get('content', {})
            if content:
                print(f"Content Type: {content.get('type', 'N/A')}")
                text_content = content.get('text', '')
                if text_content:
                    # Truncate long content for readability
                    display_text = text_content[:300] + "..." if len(text_content) > 300 else text_content
                    print(f"Content: {display_text}")
            
            # Print relevance score if available
            score = record.get('relevanceScore') or record.get('score')
            if score is not None:
                print(f"Relevance Score: {score:.4f}")
    
    def extract_all_memory_contents(self, memory_id: str, common_namespaces: Optional[List[str]] = None):
        """
        Extract and display all contents from a memory resource.
        
        Args:
            memory_id: The memory resource ID
            common_namespaces: List of common namespace patterns to try
        """
        try:
            # Print memory summary first
            self.print_memory_summary(memory_id)
            
            # Get memory details to extract namespaces from strategies
            memory = self.get_memory_details(memory_id)
            strategies = memory.get('strategies', [])
            
            # Extract namespaces from strategies
            all_namespaces = set()
            for strategy in strategies:
                namespaces = strategy.get('namespaces', [])
                all_namespaces.update(namespaces)
            
            # Add common namespaces if provided
            if common_namespaces:
                all_namespaces.update(common_namespaces)
            
            # If no namespaces found, try some common patterns
            if not all_namespaces:
                all_namespaces = {
                    "support/facts",
                    "support/customer",
                    "semantic",
                    "preferences",
                    "facts",
                    "custom"
                }
                logger.info("⚠️  No namespaces found in strategies, trying common patterns")
            
            print(f"\n🔍 EXTRACTING RECORDS FROM {len(all_namespaces)} NAMESPACES:")
            print("-" * 60)
            
            total_records = 0
            for namespace in sorted(all_namespaces):
                try:
                    print(f"\nSearching namespace: {namespace}")
                    
                    # Try to list records from this namespace
                    records = self.extract_memory_records(
                        memory_id=memory_id,
                        namespace_prefix=namespace,
                        max_results=20
                    )
                    
                    if records:
                        self.print_memory_records(records, f"RECORDS FROM NAMESPACE: {namespace}")
                        total_records += len(records)
                    else:
                        print(f"No records found in namespace: {namespace}")
                        
                except Exception as e:
                    logger.warning(f"Failed to extract from namespace '{namespace}': {e}")
                    continue
            
            print(f"\n{'='*80}")
            print(f"EXTRACTION COMPLETE - Total Records Found: {total_records}")
            print(f"{'='*80}")
            
        except Exception as e:
            logger.error(f"❌ Failed to extract all memory contents: {e}")
            raise


def main():
    """
    Main function to demonstrate memory extraction.
    """
    try:
        # Initialize the extractor
        extractor = AgentCoreMemoryExtractor(region_name="us-east-1")
        
        # List all available memories
        print("🔍 Discovering available memories...")
        memories = extractor.list_all_memories()
        
        if not memories:
            print("❌ No memories found in your account.")
            print("💡 Create a memory resource first using MemoryClient.create_memory()")
            return
        
        # Display available memories
        print(f"\n📋 AVAILABLE MEMORIES ({len(memories)}):")
        print("-" * 60)
        for i, memory in enumerate(memories, 1):
            memory_id = memory.get('memoryId') or memory.get('id')
            name = memory.get('name', 'Unnamed')
            status = memory.get('status', 'Unknown')
            print(f"{i}. ID: {memory_id}")
            print(f"   Name: {name}")
            print(f"   Status: {status}")
            print()
        
        # Extract contents from the first memory (or specify a memory ID)
        if memories:
            first_memory = memories[0]
            memory_id = first_memory.get('memoryId') or first_memory.get('id')
            
            print(f"🔍 Extracting contents from memory: {memory_id}")
            
            # Extract all contents
            extractor.extract_all_memory_contents(
                memory_id=memory_id,
                common_namespaces=[
                    "support/facts",
                    "support/customer", 
                    "support/preferences",
                    "semantic",
                    "facts",
                    "preferences"
                ]
            )
        
    except Exception as e:
        logger.error(f"❌ Memory extraction failed: {e}")
        raise


if __name__ == "__main__":
    main()