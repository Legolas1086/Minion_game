# Minion_game
solution/code for hackerrank minion game problem:
     assuming that you have understood the problem statement it is 
     a easy problem to code.
     everything in the code is  simple. Only part that may create
     confusion is the point incrementaion lines.
     Assume that initially u start to create substring from first character of the string.
     Assume the string is Minion. String length is 6.
     Now if you are at M in the string the subtring that can be created by M as starting are
     1)M
     2)Mi
     3)min
     4)mini
     5)minio
     6)minion
     string length-position of m  i.e., 6-0=6
     
     now if you are at i, the substring are:
     1)i
     2)in
     3)ini
     4)inio
     5)inion
     string length-position of i i.e., 6-1=5
     
     This is how points are incremented in the solution/code
