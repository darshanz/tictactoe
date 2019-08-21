import tkinter as tk

blocks = {}
main_window = tk.Tk()
main_window.title("Tic Tac Toe")
main_window.geometry("282x255")
btn_width = 10
btn_height = 5
turn = "X"

winning_sequences = [[1, 2, 3], [4, 5, 6], [7, 8, 9],   # horizontal matching
                     [1, 4, 7], [2, 5, 8], [3, 6, 9],  # vertical matching
                     [1, 5, 9], [3, 5, 7]]             # diagonal matching


def check_win_state():
    for sequence in winning_sequences:
        if all(blocks[symbol]['text'] == blocks[sequence[0]]['text'] and blocks[sequence[0]]['text'] != '' for symbol in sequence):
            winner = blocks[sequence[0]]['text']

            for key in sequence:
                blocks[key].configure(bg="red")

            game_over_dialog = tk.Toplevel()
            game_over_dialog.title("Game Over!!")
            game_over_dialog.geometry("200x100")
            tk.Label(game_over_dialog, text=winner + " won the game").pack()
            main_window.wait_window(game_over_dialog)

            for key in blocks:
                blocks[key]["text"] = ""
            return


def on_block_clicked(tag):
    global turn
    if blocks[tag]["text"] is "":
        blocks[tag].configure(text=turn)
        turn = "O" if turn is "X" else "X"
        check_win_state()


tag = 0
for i in range(0, 3):
    for j in range(0, 3):
        tag = tag+1
        btn = tk.Button(main_window, relief="flat", command=lambda x=tag: on_block_clicked(x))
        btn.configure(width=btn_width, height=btn_height)
        btn.grid(row=i, column=j)
        blocks[tag] = btn


main_window.mainloop()