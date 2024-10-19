<h2><a href="https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/">1545. Find Kth Bit in Nth Binary String</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b" data-immersive-translate-paragraph="1">Given two positive integers <code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">n</code> and <code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">k</code>, the binary string <code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">S<sub>n</sub></code> is formed as follows:<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定兩個正整數<code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">n</code>和<code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">k</code> ，二進位串<code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">S <sub>n</sub></code>形成如下：</font></font></font></p>

<ul>
	<li><code>S<sub>1</sub> = "0"</code></li>
	<li data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b" data-immersive-translate-paragraph="1"><code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">S<sub>i</sub> = S<sub>i - 1</sub> + "1" + reverse(invert(S<sub>i - 1</sub>))</code> for <code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">i &gt; 1</code></li>
</ul>

<p data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b" data-immersive-translate-paragraph="1">Where <code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">+</code> denotes the concatenation operation, <code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">reverse(x)</code> returns the reversed string <code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">x</code>, and <code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">invert(x)</code> inverts all the bits in <code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">x</code> (<code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">0</code> changes to <code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">1</code> and <code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">1</code> changes to <code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">0</code>).<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">其中<code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">+</code>表示串聯操作， <code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">reverse(x)</code>傳回反轉的字串<code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">x</code> ，而<code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">invert(x)</code>反轉<code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">x</code>中的所有位元（ <code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">0</code>變為<code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">1</code> ， <code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">1</code>變為<code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">0</code> ）。</font></font></font></p>

<p data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b" data-immersive-translate-paragraph="1">For example, the first four strings in the above sequence are:<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">例如，上述序列中的前四個字串是：</font></font></font></p>

<ul>
	<li><code>S<sub>1 </sub>= "0"</code></li>
	<li><code>S<sub>2 </sub>= "0<strong>1</strong>1"</code></li>
	<li><code>S<sub>3 </sub>= "011<strong>1</strong>001"</code></li>
	<li><code>S<sub>4</sub> = "0111001<strong>1</strong>0110001"</code></li>
</ul>

<p data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b" data-immersive-translate-paragraph="1">Return <em data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">the</em> <code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">k<sup>th</sup></code> <em data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">bit</em> <em data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">in</em> <code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">S<sub>n</sub></code>. It is guaranteed that <code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">k</code> is valid for the given <code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">n</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">返回<code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">S <sub>n</sub></code><em data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">中的</em><em data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">第</em><code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b"><sup>k th</sup></code><em data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">位</em>。保證<code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">k</code>對於給定的<code data-immersive-translate-walked="a955c154-ad88-4d23-9bca-94bd992da66b">n</code>有效。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> n = 3, k = 1
<strong>Output:</strong> "0"
<strong>Explanation:</strong> S<sub>3</sub> is "<strong><u>0</u></strong>111001".
The 1<sup>st</sup> bit is "0".
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> n = 4, k = 11
<strong>Output:</strong> "1"
<strong>Explanation:</strong> S<sub>4</sub> is "0111001101<strong><u>1</u></strong>0001".
The 11<sup>th</sup> bit is "1".
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 20</code></li>
	<li><code>1 &lt;= k &lt;= 2<sup>n</sup> - 1</code></li>
</ul>
</div>