class Object:
    def __init__(self, type, image, x, y, velocity_x, velocity_y):
        self.type = type
        self.image = image
        self.size = (image.get_width(), image.get_height())
        self.position = [x, y]
        self.velocity = [velocity_x, velocity_y]
    
    def out_of_bounds(self, screen_size, list):
        if self.position[0] < 0 - self.size[0] or self.position[0] > screen_size[0] or self.position[1] < 0 - self.size[1] or self.position[1] > screen_size[1]:
            list.remove(self)
            del self
    
    def collision_detection(self, objects, types):
        return next((object for object in objects if object.type in types and any(hitbox_1.colliderect(hitbox_2) for hitbox_1 in self.hitboxes for hitbox_2 in object.hitboxes)), None)
    
    def __str__(self):
        return f"object type: {self.type}"