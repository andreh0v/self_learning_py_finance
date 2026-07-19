BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS Customer (
    Customer_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS Depot(
Depot_id INT PRIMARY KEY,
Name TEXT NOT NULL,
City TEXT NOT NULL,
Country TEXT NOT NULL,
Capacity INT NOT NULL
);
CREATE TABLE IF NOT EXISTS Driver(
Driver_id INT PRIMARY KEY,
First_name TEXT  NOT NULL,
Second_name TEXT NOT NULL,
PHONE INT NOT NULL,
Driver_licence INT NOT NULL,
Vehicle_id INT NOT NULL,
Depot_id INT NOT NULL,
 FOREIGN KEY (Vehicle_id) REFERENCES Vehicle(Vehicle_id),
 FOREIGN KEY (Depot_id) REFERENCES Depot(Depot_id)
);
CREATE TABLE IF NOT EXISTS Employee (
    Employee_id INTEGER PRIMARY KEY,
    role TEXT NOT NULL,
    salary INTEGER NOT NULL,
    hire_date TEXT NOT NULL,
    Driver_id INTEGER NOT NULL,
    FOREIGN KEY (Driver_id) REFERENCES Driver(Driver_id)
);
CREATE TABLE IF NOT EXISTS Location( 
Location_id INT  PRIMARY KEY,
City TEXT NOT NULL,
Country TEXT NOT NULL,
Postal_code TEXT NOT NULL,
Address TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS Package (
    Package_id INTEGER PRIMARY KEY,
    weight_kg INTEGER NOT NULL,
    description TEXT NOT NULL,
    package_type TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS Payment (
    Payment_id INTEGER PRIMARY KEY,
    Shipment_id INTEGER NOT NULL,
    amount INTEGER NOT NULL,
    payment_date TEXT NOT NULL,
    payment_status TEXT NOT NULL,
    payment_method TEXT NOT NULL,
    FOREIGN KEY (Shipment_id) REFERENCES Shipment(Shipment_id)
);
CREATE TABLE IF NOT EXISTS Route(
Route_id INT PRIMARY KEY,
Route_name TEXT NOT NULL,
Distance_km INT NOT NULL,
Estimated_hours INT NOT NULL
);
CREATE TABLE IF NOT EXISTS RouteLocation (
    RouteLocation_id INTEGER PRIMARY KEY,
    Route_id INTEGER NOT NULL,
    Location_id INTEGER NOT NULL,
    stop_order INTEGER NOT NULL,
    FOREIGN KEY (Route_id) REFERENCES Route(Route_id),
    FOREIGN KEY (Location_id) REFERENCES Location(Location_id)
);
CREATE TABLE IF NOT EXISTS Shipment(
Shipment_id INT PRIMARY KEY,
customer_id INT NOT NULL,
Location_id INT NOT NULL,	
Driver_id	INT NOT NULL,
Vehicle_id INT NOT NULL,
Route_id INT NOT NULL,
Shipment_date 	TEXT NOT NULL, -- format 'DD-MM-YYYY'
Deliver_date TEXT NOT NULL, --format 'DD-MM-YYYY'
Status TEXT NOT NULL, --'Ordered, Packed, Shipped, Transit, Delivered,'
  FOREIGN KEY (Customer_id) REFERENCES Customer(Customer_id),
    FOREIGN KEY (Driver_id) REFERENCES Driver(Driver_id),
    FOREIGN KEY (Vehicle_id) REFERENCES Vehicle(Vehicle_id),
    FOREIGN KEY (Location_id) REFERENCES Location(Location_id),
    FOREIGN KEY (Route_id) REFERENCES Route(Route_id)
);
CREATE TABLE IF NOT EXISTS ShipmentPackage (
    ShipmentPackage_id INTEGER PRIMARY KEY,
    Shipment_id INTEGER NOT NULL,
    Package_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (Shipment_id) REFERENCES Shipment(Shipment_id),
    FOREIGN KEY (Package_id) REFERENCES Package(Package_id)
);
CREATE TABLE IF NOT EXISTS Vehicle(
Vehicle_id INT PRIMARY KEY,
Plate_num TEXT NOT NULL,
Capacity INT NOT NULL,
TYPE_CAR TEXT NOT NULL,
Depot_id INT NOT NULL,
FOREIGN KEY (Depot_id) REFERENCES Depot(Depot_id)
);
INSERT INTO "Customer" ("Customer_id","first_name","last_name","email","phone","address") VALUES (1,'Erik','Hansen','erik.hansen@email.no','91234567','Karlsbergveien 12, Oslo');
INSERT INTO "Customer" ("Customer_id","first_name","last_name","email","phone","address") VALUES (2,'Ingrid','Larsen','ingrid.larsen@email.no','92345678','Bryggen 5, Bergen');
INSERT INTO "Customer" ("Customer_id","first_name","last_name","email","phone","address") VALUES (3,'Ole','Andersen','ole.andersen@email.no','93456789','Nordre gate 8, Trondheim');
INSERT INTO "Customer" ("Customer_id","first_name","last_name","email","phone","address") VALUES (4,'Astrid','Berg','astrid.berg@email.no','94567890','Stavanger vei 3, Stavanger');
INSERT INTO "Customer" ("Customer_id","first_name","last_name","email","phone","address") VALUES (5,'Lars','Johansen','lars.johansen@email.no','95678901','Storgata 22, Tromsø');
INSERT INTO "Depot" ("Depot_id","Name","City","Country","Capacity") VALUES (1,'Oslo Depot','Oslo','Norway',500);
INSERT INTO "Depot" ("Depot_id","Name","City","Country","Capacity") VALUES (2,'Bergen Depot','Bergen','Norway',300);
INSERT INTO "Depot" ("Depot_id","Name","City","Country","Capacity") VALUES (3,'Trondheim Depot','Trondheim','Norway',400);
INSERT INTO "Depot" ("Depot_id","Name","City","Country","Capacity") VALUES (4,'Stavanger Depot','Stavanger','Norway',250);
INSERT INTO "Depot" ("Depot_id","Name","City","Country","Capacity") VALUES (5,'Tromsø Depot','Tromsø','Norway',200);
INSERT INTO "Driver" ("Driver_id","First_name","Second_name","PHONE","Driver_licence","Vehicle_id","Depot_id") VALUES (1,'Bjorn','Nielsen',91111111,'DL-001',1,1);
INSERT INTO "Driver" ("Driver_id","First_name","Second_name","PHONE","Driver_licence","Vehicle_id","Depot_id") VALUES (2,'Kari','Olsen',92222222,'DL-002',2,2);
INSERT INTO "Driver" ("Driver_id","First_name","Second_name","PHONE","Driver_licence","Vehicle_id","Depot_id") VALUES (3,'Per','Dahl',93333333,'DL-003',3,3);
INSERT INTO "Driver" ("Driver_id","First_name","Second_name","PHONE","Driver_licence","Vehicle_id","Depot_id") VALUES (4,'Siri','Holm',94444444,'DL-004',4,4);
INSERT INTO "Driver" ("Driver_id","First_name","Second_name","PHONE","Driver_licence","Vehicle_id","Depot_id") VALUES (5,'Tor','Viken',95555555,'DL-005',5,5);
INSERT INTO "Employee" ("Employee_id","role","salary","hire_date","Driver_id") VALUES (1,'Driver',450000,'2020-01-15',1);
INSERT INTO "Employee" ("Employee_id","role","salary","hire_date","Driver_id") VALUES (2,'Driver',430000,'2019-03-20',2);
INSERT INTO "Employee" ("Employee_id","role","salary","hire_date","Driver_id") VALUES (3,'Driver',460000,'2021-06-01',3);
INSERT INTO "Employee" ("Employee_id","role","salary","hire_date","Driver_id") VALUES (4,'Driver',420000,'2022-08-10',4);
INSERT INTO "Employee" ("Employee_id","role","salary","hire_date","Driver_id") VALUES (5,'Driver',470000,'2018-11-05',5);
INSERT INTO "Location" ("Location_id","City","Country","Postal_code","Address") VALUES (1,'Oslo','Norway','0150','Karlsbergveien 12');
INSERT INTO "Location" ("Location_id","City","Country","Postal_code","Address") VALUES (2,'Bergen','Norway','5003','Bryggen 5');
INSERT INTO "Location" ("Location_id","City","Country","Postal_code","Address") VALUES (3,'Trondheim','Norway','7010','Nordre gate 8');
INSERT INTO "Location" ("Location_id","City","Country","Postal_code","Address") VALUES (4,'Stavanger','Norway','4006','Stavanger vei 3');
INSERT INTO "Location" ("Location_id","City","Country","Postal_code","Address") VALUES (5,'Tromsø','Norway','9008','Storgata 22');
INSERT INTO "Package" ("Package_id","weight_kg","description","package_type") VALUES (1,5,'Electronics','Fragile');
INSERT INTO "Package" ("Package_id","weight_kg","description","package_type") VALUES (2,20,'Furniture','Large');
INSERT INTO "Package" ("Package_id","weight_kg","description","package_type") VALUES (3,2,'Documents','Standard');
INSERT INTO "Package" ("Package_id","weight_kg","description","package_type") VALUES (4,15,'Clothing','Standard');
INSERT INTO "Package" ("Package_id","weight_kg","description","package_type") VALUES (5,50,'Machinery','Heavy');
INSERT INTO "Payment" ("Payment_id","Shipment_id","amount","payment_date","payment_status","payment_method") VALUES (1,1,1500,'2024-01-10','Paid','Card');
INSERT INTO "Payment" ("Payment_id","Shipment_id","amount","payment_date","payment_status","payment_method") VALUES (2,2,2200,'2024-02-05','Paid','Bank Transfer');
INSERT INTO "Payment" ("Payment_id","Shipment_id","amount","payment_date","payment_status","payment_method") VALUES (3,3,3100,'2024-03-12','Pending','Invoice');
INSERT INTO "Payment" ("Payment_id","Shipment_id","amount","payment_date","payment_status","payment_method") VALUES (4,4,4500,'2024-04-20','Pending','Card');
INSERT INTO "Payment" ("Payment_id","Shipment_id","amount","payment_date","payment_status","payment_method") VALUES (5,5,5800,'2024-05-01','Paid','Bank Transfer');
INSERT INTO "Route" ("Route_id","Route_name","Distance_km","Estimated_hours") VALUES (1,'Oslo-Bergen',492,7);
INSERT INTO "Route" ("Route_id","Route_name","Distance_km","Estimated_hours") VALUES (2,'Bergen-Trondheim',680,9);
INSERT INTO "Route" ("Route_id","Route_name","Distance_km","Estimated_hours") VALUES (3,'Trondheim-Stavanger',890,12);
INSERT INTO "Route" ("Route_id","Route_name","Distance_km","Estimated_hours") VALUES (4,'Stavanger-Tromsø',1820,24);
INSERT INTO "Route" ("Route_id","Route_name","Distance_km","Estimated_hours") VALUES (5,'Oslo-Tromsø',1850,25);
INSERT INTO "RouteLocation" ("RouteLocation_id","Route_id","Location_id","stop_order") VALUES (1,1,1,1);
INSERT INTO "RouteLocation" ("RouteLocation_id","Route_id","Location_id","stop_order") VALUES (2,1,2,2);
INSERT INTO "RouteLocation" ("RouteLocation_id","Route_id","Location_id","stop_order") VALUES (3,2,2,1);
INSERT INTO "RouteLocation" ("RouteLocation_id","Route_id","Location_id","stop_order") VALUES (4,2,3,2);
INSERT INTO "RouteLocation" ("RouteLocation_id","Route_id","Location_id","stop_order") VALUES (5,3,3,1);
INSERT INTO "Shipment" ("Shipment_id","customer_id","Location_id","Driver_id","Vehicle_id","Route_id","Shipment_date","Deliver_date","Status") VALUES (1,1,1,1,1,1,'2024-01-10','2024-01-17','Delivered');
INSERT INTO "Shipment" ("Shipment_id","customer_id","Location_id","Driver_id","Vehicle_id","Route_id","Shipment_date","Deliver_date","Status") VALUES (2,2,2,2,2,2,'2024-02-05','2024-02-14','Delivered');
INSERT INTO "Shipment" ("Shipment_id","customer_id","Location_id","Driver_id","Vehicle_id","Route_id","Shipment_date","Deliver_date","Status") VALUES (3,3,3,3,3,3,'2024-03-12','2024-03-24','In Transit');
INSERT INTO "Shipment" ("Shipment_id","customer_id","Location_id","Driver_id","Vehicle_id","Route_id","Shipment_date","Deliver_date","Status") VALUES (4,4,4,4,4,4,'2024-04-20','2024-05-14','Ordered');
INSERT INTO "Shipment" ("Shipment_id","customer_id","Location_id","Driver_id","Vehicle_id","Route_id","Shipment_date","Deliver_date","Status") VALUES (5,5,5,5,5,5,'2024-05-01','2024-05-26','Packed');
INSERT INTO "ShipmentPackage" ("ShipmentPackage_id","Shipment_id","Package_id","quantity") VALUES (1,1,1,2);
INSERT INTO "ShipmentPackage" ("ShipmentPackage_id","Shipment_id","Package_id","quantity") VALUES (2,2,2,1);
INSERT INTO "ShipmentPackage" ("ShipmentPackage_id","Shipment_id","Package_id","quantity") VALUES (3,3,3,5);
INSERT INTO "ShipmentPackage" ("ShipmentPackage_id","Shipment_id","Package_id","quantity") VALUES (4,4,4,3);
INSERT INTO "ShipmentPackage" ("ShipmentPackage_id","Shipment_id","Package_id","quantity") VALUES (5,5,5,1);
INSERT INTO "Vehicle" ("Vehicle_id","Plate_num","Capacity","TYPE_CAR","Depot_id") VALUES (1,'AB12345',1000,'Truck',1);
INSERT INTO "Vehicle" ("Vehicle_id","Plate_num","Capacity","TYPE_CAR","Depot_id") VALUES (2,'CD23456',800,'Van',2);
INSERT INTO "Vehicle" ("Vehicle_id","Plate_num","Capacity","TYPE_CAR","Depot_id") VALUES (3,'EF34567',1200,'Truck',3);
INSERT INTO "Vehicle" ("Vehicle_id","Plate_num","Capacity","TYPE_CAR","Depot_id") VALUES (4,'GH45678',600,'Van',4);
INSERT INTO "Vehicle" ("Vehicle_id","Plate_num","Capacity","TYPE_CAR","Depot_id") VALUES (5,'IJ56789',1500,'Truck',5);
COMMIT;
