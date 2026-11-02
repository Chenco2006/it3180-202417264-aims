
# AIMS-mini Use Case Diagram

## Actor
- Customer: Người sử dụng hệ thống.

## Use Cases
- Add DVD to cart
- Remove DVD from cart
- View cart
- Calculate total cost
- Search DVD by title

## Use Case Diagram

```mermaid
flowchart LR
    Customer[Customer]

    UC1([Add DVD to cart])
    UC2([Remove DVD from cart])
    UC3([View cart])
    UC4([Calculate total cost])
    UC5([Search DVD by title])

    Customer --- UC1
    Customer --- UC2
    Customer --- UC3
    Customer --- UC4
    Customer --- UC5
```