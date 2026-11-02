from aims import __version__
from aims.dvd import DigitalVideoDisc
from aims.cart import Cart
from aims.search import search_by_title 


def main():
    print(f"AIMS-mini v{__version__}")
    cart = Cart()
    cart.add_dvd(DigitalVideoDisc("The Lion King", "Animation", "Roger Allers", 87, 19.95))
    cart.add_dvd(DigitalVideoDisc("Star Wars", "Science Fiction", "George Lucas", 87, 24.95))
    cart.add_dvd(DigitalVideoDisc("Aladdin", "Animation", cost=18.99))
    cart.print_cart()

    # Thêm đoạn tìm kiếm ngay bên dưới cart.print_cart()
    results = search_by_title(cart.items, "star")

    print("\nSearch results:")
    for dvd in results:
        print(dvd)


if __name__ == "__main__":
    main()