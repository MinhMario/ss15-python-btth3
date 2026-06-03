available_seats = 50
flight_revenue = 0.0
BASE_PRICE = 2000.0

def displayMenu():
    print('''============= SKYBOOKING SYSTEM =============
Chuyến bay: VN2026 | Khởi hành: Hà Nội
1. Đặt vé máy bay
2. Hủy vé & Hoàn tiền
3. Xem tình trạng chuyến bay
4. Đóng hệ thống
=============================================''')

def booking():
    amount = input('Nhập số lượng vé cần mua: ')
    amount = int(amount)
    global available_seats
    global flight_revenue
    if available_seats < amount or available_seats <= 0:
        print('Đã hết chỗ')
        return
    available_seats -= amount
    while True:
        type = input('Chọn hạng vé (1-2): ')
        try:
            type = int(type)
            if type != 1 and type != 2:
                print('Hạng vé không hợp lệ')
            else:
                break
        except ValueError:
            print('Không hợp lệ')
    if type == 1:
        price = BASE_PRICE
        rank = 'Economy'
    else:
        rank = 'Business'
        price = BASE_PRICE * 1.5
    flight_revenue += (price + 0.05 * price) * amount
    print(f"Xác nhận đặt chỗ:")
    print(f"Số lượng: {amount} | Hạng: {rank}")
    print(f"Tạm tính: ${price * amount}")
    print(f"Phí dịch vụ: ${0.05 * price * amount}")
    print(f"Tổng thanh toán: ${flight_revenue}")
    print(f"Đặt vé thành công! Số ghế còn lại: {available_seats}")
    return flight_revenue

def cancel_flight():
    global flight_revenue
    global available_seats
    while True:
        amount = input('Nhập số lượng vé muốn hủy: ')
        try:
            amount = int(amount)
            if amount <= 0 or available_seats + amount > 50:
                print('Số lượng không hợp lệ')
                return
            else:
                break
        except ValueError:
            print('Không hợp lệ')
    available_seats += amount
    flight_revenue -= 0.8 * BASE_PRICE * amount
    print(f"Hủy vé thành công. Hệ thống đã hoàn lại {0.8 * BASE_PRICE * amount}")
    print(f"Ghế trống hiện tại: {available_seats}")

def checkFlight():
    print('-- Tình trạng chuyến bay --')
    print('Sức chứa tối đa: 50')
    print(f"Ghế đã đặt: {50 - available_seats}")
    print(f"Ghế trống: {available_seats}")


while True:
    displayMenu()
    choice = input('Vui lòng chọn (1-4): ').strip()

    match choice:
        case '1':
            booking()
        case '2':
            cancel_flight()
        case '3':
            checkFlight()
        case '4':
            print('Cảm ơn đã sử dụng SkyBooking. Tạm biệt!')
            break
        case _:
            print('Lựa chọn không hợp lệ, vui lòng chọn từ 1 đến 4.')