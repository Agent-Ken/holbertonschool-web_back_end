-- decrease_quantity trigger that does what it says after adding a new order
CREATE TRIGGER decrease_quantity
AFTER INSERT ON orders
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE NEW.item_name = name;
