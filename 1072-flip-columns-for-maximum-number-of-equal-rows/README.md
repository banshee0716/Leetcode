<h2><a href="https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/">1072. Flip Columns For Maximum Number of Equal Rows</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="55aaaa89-76a0-4704-acaf-dded52aaec87" data-immersive-translate-paragraph="1">You are given an <code data-immersive-translate-walked="55aaaa89-76a0-4704-acaf-dded52aaec87">m x n</code> binary matrix <code data-immersive-translate-walked="55aaaa89-76a0-4704-acaf-dded52aaec87">matrix</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個<code data-immersive-translate-walked="55aaaa89-76a0-4704-acaf-dded52aaec87">mxn</code>二進位矩陣<code data-immersive-translate-walked="55aaaa89-76a0-4704-acaf-dded52aaec87">matrix</code> 。</font></font></font></p>

<p data-immersive-translate-walked="55aaaa89-76a0-4704-acaf-dded52aaec87" data-immersive-translate-paragraph="1">You can choose any number of columns in the matrix and flip every cell in that column (i.e., Change the value of the cell from <code data-immersive-translate-walked="55aaaa89-76a0-4704-acaf-dded52aaec87">0</code> to <code data-immersive-translate-walked="55aaaa89-76a0-4704-acaf-dded52aaec87">1</code> or vice versa).<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">您可以選擇矩陣中任意數量的列並翻轉該列中的每個單元格（即，將單元格的值從<code data-immersive-translate-walked="55aaaa89-76a0-4704-acaf-dded52aaec87">0</code>更改為<code data-immersive-translate-walked="55aaaa89-76a0-4704-acaf-dded52aaec87">1</code> ，反之亦然）。</font></font></font></p>

<p data-immersive-translate-walked="55aaaa89-76a0-4704-acaf-dded52aaec87" data-immersive-translate-paragraph="1">Return <em data-immersive-translate-walked="55aaaa89-76a0-4704-acaf-dded52aaec87">the maximum number of rows that have all values equal after some number of flips</em>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">傳回<em data-immersive-translate-walked="55aaaa89-76a0-4704-acaf-dded52aaec87">經過一定次數的翻轉後所有數值都相等的最大行數</em>。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> matrix = [[0,1],[1,1]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> After flipping no values, 1 row has all values equal.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> matrix = [[0,1],[1,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> After flipping values in the first column, both rows have equal values.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> matrix = [[0,0,0],[0,0,1],[1,1,0]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> After flipping values in the first two columns, the last two rows have equal values.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 300</code></li>
	<li><code>matrix[i][j]</code> is either&nbsp;<code>0</code> or <code>1</code>.</li>
</ul>
</div>