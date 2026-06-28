def sort_colors(colors):
    color_list = colors.split("-")
    color_list.sort()
    return "-".join(color_list)


print(sort_colors("green-red-yellow-black-white"))
print(sort_colors("PINK-BLUE-TAN-PURPLE"))