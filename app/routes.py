from flask import render_template, Markup, redirect, url_for
from app import app
import sys
import copy
import chessUtils as cu

@app.route('/game/<id>')
def game(id):
    board = cu.readBoardFile(str(id))
    output = Markup(cu.boardHTML(board))

    return render_template('game.html', title='Game', output=output)

@app.route('/game/<id>/move/<movestring>')
def move(id, movestring):
    board = cu.readBoardFile(str(id))

    if board == 'NONE':
        return "<html><h2>Invalid game</h2></html>"

    # move piece
    result = cu.processMove(movestring, board)

    if len(result) == 2:
        print("INFO: " + result[0] + ', ' + result[1], file=sys.stderr)
    else:
        board = result

    test_board = copy.deepcopy(board)

    cu.checkForCheck('white', test_board)
    cu.checkForCheck('black', test_board)

    cu.writeBoardFile(str(id), board)

    # re-direct to show new game state
    return redirect(url_for('game', id=id))
