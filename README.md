# Python Multiprocessing

A comprehensive guide to multiprocessing in Python, demonstrating various concepts through practical examples.

## Overview

This repository contains examples showcasing different aspects of Python's `multiprocessing` module, which allows you to write parallel code that can leverage multiple CPU cores to execute tasks concurrently.

## What is Multiprocessing?

Multiprocessing is a technique that allows a program to create multiple processes, each running independently with its own memory space. Unlike threading, which is limited by Python's Global Interpreter Lock (GIL), multiprocessing can achieve true parallelism by utilizing multiple CPU cores.

**Key Benefits:**
- Bypass the GIL limitation
- True parallel execution on multiple cores
- Better performance for CPU intensive tasks
- Isolated memory spaces prevent interference between processes

## Files Overview

### 1. `process.py`
**Basic Process Creation and Management**

Demonstrates the fundamental concepts of creating and managing multiple processes.

**Key Concepts:**
- Creating `Process` objects with target functions
- Using `os.cpu_count()` to determine available CPU cores
- Starting processes with `start()`
- Waiting for process completion with `join()`

**What it does:** Creates multiple processes (equal to the number of CPU cores) that each execute a simple computation task concurrently.

---

### 2. `process_pool.py`
**Process Pool for Efficient Task Distribution**

Shows how to use `Pool` for managing a pool of worker processes, which is more efficient than creating processes manually for multiple tasks.

**Key Concepts:**
- `Pool()` creates a pool of worker processes
- `map()` distributes tasks across the pool
- `close()` prevents new tasks from being submitted
- `join()` waits for all workers to finish

**What it does:** Computes the cube of numbers from 0-9 using a process pool, distributing the work across available CPU cores.

**Advantages of Pool:**
- Automatic process management
- Efficient reuse of worker processes
- Simplified parallel execution of functions

---

### 3. `queue_usage.py`
**Inter-Process Communication with Queues**

Demonstrates how processes can communicate and share results using `Queue`, which is a thread and process-safe FIFO queue.

**Key Concepts:**
- `Queue()` for safe inter-process communication
- `put()` to add items to the queue
- `get()` to retrieve items from the queue
- `empty()` to check if the queue is empty

**What it does:** Two processes perform different operations (squaring and negating numbers) and put their results into a shared queue, which is then read by the main process.

**Use Cases:**
- Collecting results from multiple processes
- Producer-consumer patterns
- Distributing work items to processes

---

### 4. `single_value_data_sharing.py`
**Shared Memory - Single Value with Lock**

Shows how to share a single value between processes using `Value` and protect it from race conditions using `Lock`.

**Key Concepts:**
- `Value()` creates a shared memory variable
  - `'i'` denotes signed integer type
  - Other types: `'d'` (double), `'f'` (float), etc.
- `Lock()` ensures mutual exclusion
- `with lock:` context manager for automatic lock acquisition and release
- Race conditions and why synchronization is necessary

**What it does:** Two processes each increment a shared counter 100 times. Without the lock, race conditions could cause incorrect results (not reaching 200). With the lock, the final value is guaranteed to be 200.

**Race Condition Example:**
Without proper locking, both processes might read the same value simultaneously, increment it and write back, causing lost updates.

---

### 5. `multi_value_data_sharing.py`
**Shared Memory - Array with Lock**

Demonstrates sharing multiple values using `Array`, which is similar to `Value` but for collections of data.

**Key Concepts:**
- `Array()` creates a shared memory array
  - First parameter: type code (`'d'` for double, `'i'` for integer)
  - Second parameter: initial values
- Accessing array elements with indexing
- Protecting array modifications with locks
- Iterating over shared arrays safely

**What it does:** Two processes each increment all elements of a shared array [0.0, 100.0, 200.0] by 1, doing this 100 times. The final result is [200.0, 300.0, 400.0].

**Important:** The lock protects the entire inner loop to ensure all array elements are updated atomically by one process at a time.

## Usage

Each file can be run independently:

```bash
python process.py
python process_pool.py
python queue_usage.py
python single_value_data_sharing.py
python multi_value_data_sharing.py
```

## When to Use Multiprocessing

**Good for:**
- CPU-intensive tasks (computation, data processing)
- Tasks that can be parallelized
- Bypassing the GIL limitation

**Not ideal for:**
- I/O-bound tasks (use `asyncio` or threading instead)
- Tasks requiring frequent inter-process communication
- Memory-intensive applications (each process has its own memory)

## Common Pitfalls

1. **Forgetting to use locks:** Can lead to race conditions and incorrect results
2. **Not calling `join()`:** Main process may exit before child processes complete
3. **Pickling issues:** Objects passed between processes must be serializable
4. **Overhead:** Creating processes has overhead; not worth it for trivial tasks

## Requirements

- Python 3.x
- No external dependencies (uses standard library only)

## Learning Path

1. Start with `process.py` to understand basic process creation
2. Move to `process_pool.py` for efficient task distribution
3. Learn inter-process communication with `queue_usage.py`
4. Understand shared memory with `single_value_data_sharing.py`
5. Explore arrays in shared memory with `multi_value_data_sharing.py`


**Note:** The `time.sleep(0.01)` calls in the data sharing examples simulate real work and make race conditions more visible without locks.

## License
- This is my example code for learning purposes. Use freely.