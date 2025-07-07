import heapq
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        pq = []
        i, n, ans = 0, len(events), 0
        
        # Calculate the maximum day from the events to iterate through days
        mxday = 0
        if events: # Ensure events list is not empty before finding max day
            mxday = max(event[1] for event in events)
        
        for day in range(1, mxday + 1):
            # Add all events that start on or before the current day to the min-heap
            # The heap stores end days, so the earliest ending event is at the top.
            while i < n and events[i][0] <= day:
                heapq.heappush(pq, events[i][1])
                i += 1
            
            # Remove events that have already ended (their end day is less than current day)
            while pq and day > pq[0]:
                heapq.heappop(pq)
            
            # If there are events available to attend on this day, attend the one
            # that ends earliest (which is at the top of the min-heap).
            if pq:
                heapq.heappop(pq) # Attend this event
                ans += 1
        return ans

def get_events_input() -> List[List[int]]:
    events = []
    print("Enter events. Each event should be 'start_day,end_day' (e.g., '1,2').")
    print("Type 'done' when you have finished entering events.")
    
    while True:
        event_str = input("Event: ").strip()
        if event_str.lower() == 'done':
            break
        if not event_str:
            continue
        try:
            start, end = map(int, event_str.split(','))
            if start <= 0 or end <= 0 or start > end:
                print("Invalid days. Start and end days must be positive, and start_day <= end_day.")
                continue
            events.append([start, end])
        except ValueError:
            print("Invalid format. Please enter two integers separated by a comma (e.g., '1,2').")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")
    return events

if __name__ == "__main__":
    sol = Solution()

    print("--- Max Events Attended ---")
    
    events_input = get_events_input()
    
    if not events_input:
        print("No events entered. Maximum events attended: 0")
    else:
        result = sol.maxEvents(events_input)
        print(f"\nThe maximum number of events that can be attended is: {result}")