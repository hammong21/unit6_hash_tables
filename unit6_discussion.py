"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""

def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key‑value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    # 1. Create an empty dictionary to serve as our hash table.
    hash_table = {}                                 
    # 2. Insert five entries (key: student name, value: favorite food)
    hash_table["alice"]   = "sushi"
    hash_table["bob"]     = "tacos"
    hash_table["carol"]   = "pizza"
    hash_table["dave"]    = "ramen"
    hash_table["eve"]     = "salad"

    # -----------------------------------------------------------------
    # 3️⃣  How a Python dict behaves like a hash table
    # -----------------------------------------------------------------
    # * When a key is inserted, Python runs the key through a built‑in
    #   hash function (`hash(key)`). The resulting integer is then
    #   reduced modulo the current table size to select a bucket.
    # * The bucket holds the (key, value) pair. If two different keys
    #   produce the same bucket index causing a collision, CPython resolves it
    #   with open‑addressing and a compact array layout.
    # * Because the hash index gives direct access to the bucket,
    #   lookups, updates, and deletions are **average‑case O(1)** – the
    #   same constant‑time performance you get from a classic hash table.
    # -----------------------------------------------------------------v

    # 4. display current contents
    print("\n=== INSERT OPERATIONS ===")
    print("Created hash table (dictionary) with 5 entries:")
    
    for k, v in hash_table.items():
        print(f"  {k!r} → {v!r}")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    # ---- Implementation -------------------------------------------------
    print("\n=== LOOKUP OPERATIONS ===")
    # Lookup two known keys; the dict uses the key's hash to jump
    # directly to the stored value (average‑case O(1)).
    alice_food = hash_table["alice"]
    bob_food   = hash_table["bob"]

    print(f"Lookup result – alice's favorite food: {alice_food}")
    print(f"Lookup result – bob's favorite food:   {bob_food}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    # ---- Implementation -------------------------------------------------
    print("\n=== UPDATE OPERATIONS ===")
    print("Dictionary before update:", hash_table)
    # Assigning a new value to an existing key overwrites the old entry
    # without changing the key's bucket.
    
    hash_table["carol"] = "pasta"
    print("Dictionary after updating 'carol':", hash_table)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    # Requirements:
    # 1. Delete at least one key‑value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    # ---- Implementation -------------------------------------------------
    print("\n=== DELETE OPERATIONS ===")
    print("Dictionary before deletion:", hash_table)

    # `del` removes the entry and frees the bucket for future inserts.
    del hash_table["dave"]
    print("Dictionary after deleting 'dave':", hash_table)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    # ---- Implementation -------------------------------------------------
    print("\n=== EDGE CASES ===")
    # 1. Lookup a missing key – raises KeyError; using .get() avoids it.
    missing = hash_table.get("frank")
    print("Attempted lookup for missing key 'frank' using .get():", missing)

    # 2. Delete a missing key – using pop with default avoids KeyError.
    removed = hash_table.pop("frank", None)
    print("Attempted deletion of missing key 'frank' using pop():", removed)

    # 3. Update a missing key – simple assignment creates the entry.
    hash_table["grace"] = "burger"
    print("After assigning a value to a previously‑missing key 'grace':", hash_table)

    # 4. Operate on an empty dictionary.
    empty_dict = {}
    print("Empty dictionary lookup using .get():", empty_dict.get("any"))

if __name__ == "__main__":
    main()