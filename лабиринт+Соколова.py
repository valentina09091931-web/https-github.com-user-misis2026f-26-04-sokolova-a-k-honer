import random
SYMBOLS = {
    "empty": " ",
    "monster": "M",
    "weapon": "W",
    "treasure": "$",
    "key": "K",
    "princess": "P",
    "trap": "T",
}

class Player:
    def __init__(self):
        self.r=0
        self.c=0
        self.hp=200
        self.w=False
        self.k=False
        self.p=False
        self.t=0
    def move(self,dr,dc,size):
        nr=self.r+dr
        nc=self.c+dc
        if nr<0 or nr>=size:
            return False
        if nc<0 or nc>=size:
            return False
        self.r=nr
        self.c=nc
        return True
    def take_damage(self):
        self.hp=self.hp-50
        if self.hp<0:
            self.hp=0
        return self.hp
    def is_alive(self):
        if self.hp>0:
            return True
        if self.hp==0:
            return False
    def status(self):
        self.max_hp=200
        print("HP:", self.hp, "/", self.max_hp,
              "|Оружие:", self.w,
              "|Ключ:", self.k,
              "|Принцесса:", self.p,
              "|Сокровища:", self.t)
class Cell:
    def __init__(self, content="empty"):
        self.content=content
        self.visited=False
    def symbol(self):
        if not self.visited:
            return "."
        return SYMBOLS.get(self.content, "?")
class Maze:
    def __init__(self, size=5):
        self.size=size
        self.grid=[]
        self.generate()
    def generate(self):
        self.grid=[]
        for rr in range(self.size):
            r=[]
            for cc in range(self.size):
                r.append(Cell())
            self.grid.append(r)
        positions=[]
        for rr in range(self.size):
            for cc in range(self.size):
                is_start=(rr==0 and cc==0)
                is_finish=(rr==self.size-1 and cc==self.size-1)
                if not is_start and not is_finish:
                    positions.append((rr,cc))
                random.shuffle(positions)
        required=["monster","weapon","key","princess","trap","treasure"]
        for content in required:
            r,c=positions.pop()
            self.grid[r][c].content=content
        extra=["empty","trap","monster","treasure"]
        while positions:
            r,c=positions.pop()
            self.grid[r][c].content=random.choice(extra)
    def get(self,r,c):
        return self.grid[r][c]
    def show(self,player):
        print("/n 0 1 2 3 4")
        for rr in range(self.size):
            line=str(rr)+" "
            for cc in range(self.size):
                if rr==player.r and cc==player.c:
                    line=line+"@ "
                else:
                    line=line+self.grid[rr][cc].symbol()+" "
            print(line)
class Game:
    def __init__(self):
        self.size=5
        self.maze=Maze(self.size)
        self.player=Player()
        self.maze.get(0,0).visited=True
        self.finished=False
        self.won=False
    def enter_cell(self):
        cell=self.maze.get(self.player.r,self.player.c)
        cell.visited=True
        content=cell.content
        cell.content="empty"
        if content=="weapon":
            self.player.w=True
            print("Вы нашли оружие")
        elif content=="key":
            self.player.k=True
            print("Вы нашли ключ")
        elif content=="princess":
            self.player.p=True
            print("Вы спасли принцессу")
        elif content=="treasure":
            self.player.t+=1
            print("Вы нашли сокровище! Всего:", self.player.t)
        elif content=="trap":
            self.player.take_damage()
            print("Ловушка! -50 HP")
        elif content=="monster":
            if self.player.w:
                print("Монстр побеждён! У вас было оружие")
            else:
                self.player.take_damage()
                print("Монстр! У вас нет оружие -50 HP")
    def check_finish(self):
        last=self.size-1
        if self.player.r==last and self.player.c==last:
            if self.player.k:
                self.won=True
                self.finished=True
                print("Вы вышли из лабиринта!")
            else:
                print("Это выход, но у вас нет ключа!")
    def run(self):
        print("Цель: найти ключ (K) и дойти до правого нижнего угла.")
        print("Управление: w/a/s/d, q — выход")
        while not self.finished:
            self.maze.show(self.player)
            self.player.status()
            command=input("Ваш ход:").strip().lower()
            if command=="q":
                return
            moves={"w":(-1,0), "s":(1,0), "a":(0,-1), "d":(0,1)}
            if command not in moves:
                print("Неизвестная команда")
                continue
            dr,dc=moves[command]
            if not self.player.move(dr,dc,self.size):
                print("За границу нельзя!")
                continue
            self.enter_cell()
            if not self.player.is_alive():
                print("Вы погибли")
                self.finished=True
                break
            self.check_finish()
            if self.won:
                print("\nПОБЕДА! Сокровищ:", self.player.t,
                      "|HP:", self.player.hp)
                if self.player.p:
                    print("Принцессв спасена!")
game=Game()
game.run()
