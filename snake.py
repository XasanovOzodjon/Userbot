import asyncio
import random
from telethon import events

def setup(client):

    @client.on(events.NewMessage(pattern="!snake", outgoing=True))
    async def snake_handler(event):
        await event.delete()
        
        head = "👽"
        body = "🟩"
        food = "🍎"
        empty = "⬛"
        
        size = 8
        
        snake = [(0, 0), (0, 1), (0, 2)]
        
        def get_empty_cells():
            empty_cells = []
            for r in range(size):
                for c in range(size):
                    if (r, c) not in snake:
                        empty_cells.append((r, c))
            return empty_cells
        
        def spawn_food():
            empty_cells = get_empty_cells()
            if empty_cells:
                return random.choice(empty_cells)
            return None
        
        current_food = spawn_food()
        
        def get_new_direction():
            hr, hc = snake[-1]
            
            possible = [
                (0, 1),
                (0, -1),
                (1, 0),
                (-1, 0),
            ]
            
            safe_directions = []
            food_directions = []
            
            for dr, dc in possible:
                new_r, new_c = hr + dr, hc + dc
                
                if (0 <= new_r < size and 0 <= new_c < size and (new_r, new_c) not in snake):
                    safe_directions.append((dr, dc))
                    
                    if current_food:
                        old_dist = abs(hr - current_food[0]) + abs(hc - current_food[1])
                        new_dist = abs(new_r - current_food[0]) + abs(new_c - current_food[1])
                        if new_dist < old_dist:
                            food_directions.append((dr, dc))
            
            if food_directions:
                return random.choice(food_directions)
            elif safe_directions:
                return random.choice(safe_directions)
            else:
                return possible[0]
        
        def draw():
            field = [[empty for _ in range(size)] for _ in range(size)]
            
            if current_food:
                field[current_food[0]][current_food[1]] = food
            
            for r, c in snake[:-1]:
                if 0 <= r < size and 0 <= c < size:
                    field[r][c] = body
            
            hr, hc = snake[-1]
            if 0 <= hr < size and 0 <= hc < size:
                field[hr][hc] = head
            
            return "\n".join("".join(row) for row in field)
        
        msg = await event.respond(draw())
        
        start_time = asyncio.get_event_loop().time()
        game_duration = 15
        
        while True:
            elapsed = asyncio.get_event_loop().time() - start_time
            if elapsed >= game_duration:
                break
            
            await asyncio.sleep(0.3)
            
            direction = get_new_direction()
            dr, dc = direction
            
            new_head = (snake[-1][0] + dr, snake[-1][1] + dc)
            
            if not (0 <= new_head[0] < size and 0 <= new_head[1] < size):
                break
            
            if new_head in snake:
                break
            
            snake.append(new_head)
            
            if new_head == current_food:
                current_food = spawn_food()
            else:
                snake.pop(0)
            
            try:
                await msg.edit(draw())
            except:
                break
        
        await asyncio.sleep(0.3)
        try:
            await msg.delete()
        except:
            pass