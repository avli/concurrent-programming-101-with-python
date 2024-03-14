import time
from collections import deque


def stm_delay(context):
    if context['state'] == 0:
        seconds = context['seconds']
        context['start'] = time.time()
        context['end'] = context['start'] + seconds
        context['state'] = 1
        return
    elif context['state'] == 1:
        end = context['end']
        if time.time() >= end:
            print('Done!')
            context['is_finished'] = True
        else:
            print('Too early...')


if __name__ == '__main__':
    task_queue = deque()
    for _ in range(5):
        context = {'seconds': 1, 'state': 0, 'is_finished': False}
        task_queue.append((context, stm_delay))
    while task_queue:
        context, task = task_queue.popleft()
        task(context)
        if not context['is_finished']:
            task_queue.append((context, task))
        time.sleep(0.1)
