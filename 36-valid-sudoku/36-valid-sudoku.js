/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
  
    let rowHash = [], colHash = [], boxHash = {};
    
    for(let i=board.length-1; i>=0; i--) {
        if(!rowHash[i]) 
            rowHash[i] = {};
        for(let j=board[i].length - 1; j>=0; j--){
            let num = board[i][j];
            
            if(num == ".") continue;
            
            if(!colHash[j]) 
                colHash[j] = {};    
            
            let [boxI, boxJ] = getBox(i, j);
            
            if(!boxHash[boxI +"-" + boxJ])
                boxHash[boxI +"-" + boxJ] = {};
            
            if(rowHash[i][num] || colHash[j][num] || boxHash[boxI +"-" + boxJ][num]) 
                return false; 

            rowHash[i][num] = 1;
            colHash[j][num] = 1;
            boxHash[boxI +"-" + boxJ][num] = 1;
        }
    }
    
    return true;
};

function getBox(i,j) {
    return [Math.floor(i/3), Math.floor(j/3)] 
}