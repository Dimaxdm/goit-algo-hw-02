from queue import Queue
import random
import time

### Constans
SIMULATION_REQUEST_QUANTITY: int = 10   # Number of simulations (pcs)
PROCESSING_TIME: float = 0.2            # Processing time of simulation (sec)
CATEGORIES: list[str] = [               # Examples of categories for random selection.
    "Billing", 
    "Returns",
    "Complains",
    "Technical Support", 
    "General Inquiry"
]

### Variables
request_queue = Queue()
request_counter: int = 0

### Functions
def generate_request() -> dict:
    """ Create a new request and push it into the queue"""
    global request_counter
    request_counter += 1        # used as id number
    request = {                 # a new request creation
        "id": request_counter, 
        "category": random.choice(CATEGORIES), 
        "created_time": time.strftime("%H:%M:$S"),
    }
    request_queue.put(request)  # put created request to the queue
    print(f"{'[GENERATED]':<14} -> ID: {request["id"]:05d} | Category: {request["category"]}")
    return request


def process_request() -> dict | None:
    """ Process and remove a next element from the queue"""
    # return None if queue is empty 
    if request_queue.empty():
        print("[EMPTY QUEUE -> nothing to process.]")
        return None

    request = request_queue.get()
    time.sleep(PROCESSING_TIME)     # processing time simulation
    print(f"{'[PROCESSED]':<14} -> ID: {request["id"]:05d} | Category: {request["category"]}")
    return request


def service_senter_simulation(simulation_request_quantity: int = 5) -> None:
    """
    Generates requests (`simulation_request_quantity` number of times)
    Process all currently queued requests.
    """
    print("~ SERVICE CENTER QUEUE SIMULATION ~", "\n")
    # request generator
    for _ in range(simulation_request_quantity):
        generate_request()
    print("\n")
    # processing 
    while not request_queue.empty():
        process_request()
    print("\n", f"Simulation complited. The total quantity of requests is {request_counter}")


if __name__ == "__main__":
    service_senter_simulation(SIMULATION_REQUEST_QUANTITY)