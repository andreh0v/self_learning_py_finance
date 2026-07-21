This is a explanation of BAN401 task 6.
There are other files that focueses on the BAN401 term paper given in the class.
The class has been rebranded from BAN401 too STR467.
It is the same class, but now given under the Strategi & Ledelse profile for the NHH MBA.

# BAN401 Problem 6 - Transport & Logistics Database

## Database Description
This database models a Norwegian transport and logistics company.
It tracks customers, shipments, drivers, vehicles, depots, routes, packages and payments.

## Industry
Transportation & Logistics

## Tables (12 total)
- **Customer** - stores customer contact information
- **Depot** - warehouses where vehicles and drivers are based
- **Vehicle** - trucks and vans assigned to depots
- **Driver** - drivers assigned to vehicles and depots
- **Employee** - employment records for drivers (1:1 with Driver)
- **Location** - delivery destinations
- **Route** - predefined routes between locations
- **Shipment** - core table linking customers, drivers, vehicles, routes and locations
- **Payment** - one payment per shipment (1:1 with Shipment)
- **Package** - items being shipped
- **ShipmentPackage** - junction table for Shipment/Package N:N relationship
- **RouteLocation** - junction table for Route/Location N:N relationship

## Relationships
- 1:1: Driver↔Vehicle, Driver↔Employee, Shipment↔Payment
- 1:N: Customer→Shipment, Depot→Vehicle, Depot→Driver
- N:N: Shipment↔Package, Route↔Location