class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Each index holds a list for chaining

    def _hash(self, key):
        """Hash function that converts key to a table index."""
        return hash(key) % self.size

    def insert(self, key, value):
        """Insert or update a key-value pair in the hash table."""
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing key
                return

        bucket.append((key, value))  # Add new key-value pair

    def get(self, key):
        """Retrieve the value for a given key, or return None."""
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    def delete(self, key):
        """Remove the key-value pair from the table, if it exists."""
        index = self._hash(key)
        bucket = self.table[index]

        for i, (k, _) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False


# Run a simple test of the hash table
if __name__ == "__main__":
	ht = HashTable()

	ht.insert("apple", 10)
	ht.insert("banana", 20)
	ht.insert("orange", 30)

	print("Get 'apple':", ht.get("apple"))
	print("Get 'banana':", ht.get("banana"))

	ht.delete("banana")
	print("Get 'banana' after delete:", ht.get("banana"))

	ht.insert("apple", 99)
	print("Get updated 'apple':", ht.get("apple"))

	print("Hash Table Buckets:", ht.table)