<h2><a href="https://leetcode.com/problems/count-square-submatrices-with-all-ones/">1277. Count Square Submatrices with All Ones</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="a9bed9ca-d26f-4333-b16c-9fef828ccd5c" data-immersive-translate-paragraph="1">Given a <code data-immersive-translate-walked="a9bed9ca-d26f-4333-b16c-9fef828ccd5c">m * n</code> matrix of ones and zeros, return how many <strong data-immersive-translate-walked="a9bed9ca-d26f-4333-b16c-9fef828ccd5c">square</strong> submatrices have all ones.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個由 1 和 0 組成的<code data-immersive-translate-walked="a9bed9ca-d26f-4333-b16c-9fef828ccd5c">m * n</code>矩陣，傳回有多少個全為 1 的<strong data-immersive-translate-walked="a9bed9ca-d26f-4333-b16c-9fef828ccd5c">方子</strong>矩陣。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> matrix =
[
&nbsp; [0,1,1,1],
&nbsp; [1,1,1,1],
&nbsp; [0,1,1,1]
]
<strong>Output:</strong> 15
<strong>Explanation:</strong> 
There are <strong>10</strong> squares of side 1.
There are <strong>4</strong> squares of side 2.
There is  <strong>1</strong> square of side 3.
Total number of squares = 10 + 4 + 1 = <strong>15</strong>.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
<strong>Output:</strong> 7
<strong>Explanation:</strong> 
There are <b>6</b> squares of side 1.  
There is <strong>1</strong> square of side 2. 
Total number of squares = 6 + 1 = <b>7</b>.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= arr.length&nbsp;&lt;= 300</code></li>
	<li><code>1 &lt;= arr[0].length&nbsp;&lt;= 300</code></li>
	<li><code>0 &lt;= arr[i][j] &lt;= 1</code></li>
</ul>
</div>