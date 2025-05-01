from sortedcontainers import SortedList

def max_task_assign_interactive():
    """
    Takes task and worker information as input from the user and
    calculates the maximum number of tasks that can be assigned.
    """
    try:
        tasks_str = input("Enter the task strengths (comma-separated): ")
        tasks = sorted([int(t.strip()) for t in tasks_str.split(',')])

        workers_str = input("Enter the worker strengths (comma-separated): ")
        workers = sorted([int(w.strip()) for w in workers_str.split(',')])

        pills = int(input("Enter the number of pills available: "))
        strength = int(input("Enter the strength increase from a pill: "))

        def can_complete(k: int, pills_left: int) -> bool:
            """Returns True if we can finish k tasks."""
            sorted_workers = SortedList(workers[-k:])
            temp_pills = pills_left

            for i in range(k):
                task_strength = tasks[i]
                worker_index = sorted_workers.bisect_left(task_strength)

                if worker_index < len(sorted_workers):
                    sorted_workers.pop(worker_index)
                elif temp_pills > 0:
                    if sorted_workers and sorted_workers[0] + strength >= task_strength:
                        sorted_workers.pop(0)
                        temp_pills -= 1
                    else:
                        return False
                else:
                    return False
            return True

        ans = 0
        l = 0
        r = min(len(tasks), len(workers))

        while l <= r:
            m = (l + r) // 2
            if can_complete(m, pills):
                ans = m
                l = m + 1
            else:
                r = m - 1

        print(f"Maximum number of tasks that can be assigned: {ans}")

    except ValueError:
        print("Invalid input. Please enter comma-separated integers for tasks and workers, and integer values for pills and strength.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    max_task_assign_interactive()
