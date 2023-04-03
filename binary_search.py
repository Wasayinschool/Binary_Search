li = [2, 3, 5, 4, 8, 9]
query = 4

# def binary_search(list, query):
cards = sorted(li)
print(cards)
def locate_cards(cards, query):
    mn, mx = 0, (len(cards)-1)
    while mn <= mx:
        mid = (mn + mx) // 2
        mid_number = cards[mid]
    # print(mid_number)
        if mid_number== query:
            print(mid)
        elif mid_number > query:
            mx = mid - 1
        elif mid_number < query:
            mn = mid + 1
        
        return -1
        
        
locate_cards(cards, query)
    
