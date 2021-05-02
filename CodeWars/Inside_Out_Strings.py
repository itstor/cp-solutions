def inside_out(st):
    text = st.split(" ")
    result = []
    for i in text:
        lenght = len(i)
        if lenght % 2 == 0:
            result.append(i[::-1][int(lenght/2):] + i[::-1][:int(lenght/2)])
        else:
            result.append(i[::-1][int(lenght/2)+1:] + i[int(lenght/2)] +
                          i[::-1][:int(lenght/2)])

    return " ".join(str(i) for i in result)
