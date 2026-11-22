# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real‑world scenario.

## Discussion Board Reflection

Working through the dictionary‑as‑hash‑table exercise reinforced how a hash table provides constant‑time average lookup, insertion, and deletion by converting a key into a hash value that indexes a bucket. I learned to think of the dictionary’s hash(key) % size operation as the reservation system that instantly points to where a record lives, just as a restaurant host locates a booking.  

The biggest challenge was handling edge cases, specifically, dealing with missing keys without raising KeyError. Using dict.get() and pop() gave me safe fall‑backs and highlighted the importance of defensive programming when hash tables encounter absent entries. Understanding collisions when two distinct keys map to the same bucket helped me appreciate Python’s internal open addressing strategy, which keeps performance high even under load. The assignment clarified why hash tables are crucial for fast data retrieval in real world systems such as user profile lookups, inventory management, and gaming leaderboards, where large datasets could result in long data load/save times if algorithms are not efficient. 
