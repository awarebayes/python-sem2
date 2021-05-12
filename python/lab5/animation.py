class NoAnimation:
    
    def update(self):
        pass

class Rotation:
    def __init__(self, speed=0, min=None, max=None):
        self.speed = speed
        if min:
            self.rotation = min
        else:
            self.rotation = 0
        self.min = min
        self.max = max
        self.on_end_cb = lambda: None
        self.back_on_start_cb = lambda: None
    
    def on_end(self, callback):
        self.on_end_cb = callback
        return self
    
    def back_on_start(self, callback):
        self.back_on_start_cb = callback
        return self
    
    def update(self):
        if self.speed > 0 and self.max is not None:
            if self.rotation + self.speed > self.max:
                self.speed *= -1
                self.on_end_cb()
        elif self.speed < 0 and self.min is not None:
            if self.rotation + self.speed < self.min:
                self.speed *= -1
                self.back_on_start_cb()
        self.rotation += self.speed

class Linear:
    def __init__(self, speed, start_x, start_y, end_x, end_y):
        assert start_x <= end_x
        assert start_y <= end_y

        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.v_x = (end_x - start_x) * speed
        self.v_y = (end_y - start_y) * speed
        self.x = start_x
        self.y = start_y
        self.direction = 1
        self.on_end_cb = lambda: ()
        self.back_on_start_cb = lambda: ()

    def on_end(self, callback):
        self.on_end_cb = callback
        return self
    
    def back_on_start(self, callback):
        self.back_on_start_cb = callback
        return self

    def update(self):
        new_x = self.x + self.v_x * self.direction
        new_y = self.y + self.v_y * self.direction

        if self.direction > 0:
            if new_x > self.end_x or new_y > self.end_y:
                self.direction *= -1
                self.on_end_cb()
                return (0, 0)
        elif self.direction < 0:
            if new_x < self.start_x or new_y < self.start_y:
                self.direction *= -1
                self.back_on_start_cb()
                return (0, 0)

        self.x = new_x
        self.y = new_y



        

