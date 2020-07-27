# LuciferCipher

<p> Here is the Lucifer Cipher Encryption-Decryption using Python 3, the program is still in indonesian and i haven't done translate yet :D, and for the algorithm i use is from <a href = "https://www.researchgate.net/publication/338673259_PENINGKATAN_KEAMANAN_DATA_TEKS_TERENKRIPSI_ALGORITMA_LUCIFER_MENGGUNAKAN_STEGANOGRAFI_GIFSHUFFLE_PADA_CITRA"> here </a>, it's in indonesian ,or you can watch it in <a href = "http://www.quadibloc.com/crypto/co0401.htm"> here </a> for the english one  </p>
<hr>
<h4>Lucifer Algorithm steps :</h4>
<ol>
  <li> Plaintext is divided into two parts namely Left bit (L0) and Right bit (R0).</li>
  <li> Perform the first calculation using the formula: <br> 𝑅𝑖+1 = 𝐿𝑖 ⊕ 𝐹(𝑅𝑖
,𝐾𝑖
) <br> 
to find the value of R and the results will be used for 𝑅1 in the second round   </li>
  <li> Untuk mencari nilai L menggunakan rumus : <br> 𝐿𝑖+1 = 𝑅𝑖 </li>
  <li> 
After each round except the last one, the right and left sides of the block are switched</li></ol>

<p>The above process is repeated 16 rounds each. Based on the description above, it appears that in
implementation, the Lucifer algorithm has used permutation and iteration functions. The purpose of functions
This can make it difficult for cryptanalysis to solve the ciphertext produced. </p>
<p>A key byte access schedule is a schedule setting for accessing key bits in the Lucifer algorithm, where
the maximum length of a Message Byte is 8, and the C-I-D round has a maximum capacity of 16 rounds and Key
Bytes have a maximum capacity of 15 starting from 0 </p>
<hr>

<p> there are 2 file in here which is the lucifer1.py(without GUi) and the lucifer2.py (with GUI) </p>
<p> how to use : </p>
<ul>
  <li> if u running the lucifer2.py dont forget to install tkinter </li>
  <li> the plaintext, ciphertext, and key should be 16 char long </li>
<br>
<p> enjoy guys, you can watch the full explanation by watching <a href= "https://youtu.be/CG57-dA3b0U" > this </a>
