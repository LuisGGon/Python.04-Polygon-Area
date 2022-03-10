class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __repr__(self):
        return 'Rectangle(width={0.width!r}, height={0.height!r})'.format(self)
        
    def set_height(self,new_height):
        self.height = new_height
        
    def set_width(self,new_width):
        self.width = new_width

    def get_area(self):
        w = self.width
        h = self.height
        A = w*h
        return A
    
    def get_perimeter(self):
        w = self.width
        h = self.height
        P = 2*(w + h)
        return P
    
    def get_diagonal(self):
        w = self.width
        h = self.height
        D = (w**2 + h**2)**0.5
        return D
    
    def get_picture(self):
        
        w = self.width
        h = self.height
        
        if w > 50 or h>50:
            return 'Too big for picture.'
        else:
            side = w*'*'+ '\n'
            pic = h*side
            return pic
        
    def get_amount_inside(self, rect):
        
        w1 = self.width
        h1 = self.height
        w2 = rect.width
        h2 = rect.height
        
        if h1 > h2  and w1>w2:
            times = (w1*h1)//(w2*h2)
            return times
        else:
            return 0

class Square(Rectangle):
    
    def __init__(self, side):
        super().__init__(side, side)
        
    def __repr__(self):
        return 'Square(side={0.width!r})'.format(self)
    
    def set_side(self, new_side):
        self.height = new_side
        self.width = new_side
        
    def set_height(self,new_height):
        self.set_side(new_height)
        
    def set_width(self,new_width):
        self.set_side(new_width)
        