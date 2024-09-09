<h2><a href="https://leetcode.com/problems/spiral-matrix-iv/">2326. Spiral Matrix IV</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="79cfcb01-19f4-44d7-931d-fe66a1ca65bd" data-immersive-translate-paragraph="1">You are given two integers <code data-immersive-translate-walked="79cfcb01-19f4-44d7-931d-fe66a1ca65bd">m</code> and <code data-immersive-translate-walked="79cfcb01-19f4-44d7-931d-fe66a1ca65bd">n</code>, which represent the dimensions of a matrix.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定兩個整數<code data-immersive-translate-walked="79cfcb01-19f4-44d7-931d-fe66a1ca65bd">m</code>和<code data-immersive-translate-walked="79cfcb01-19f4-44d7-931d-fe66a1ca65bd">n</code> ，它們表示矩陣的維度。</font></font></font></p>

<p data-immersive-translate-walked="79cfcb01-19f4-44d7-931d-fe66a1ca65bd" data-immersive-translate-paragraph="1">You are also given the <code data-immersive-translate-walked="79cfcb01-19f4-44d7-931d-fe66a1ca65bd">head</code> of a linked list of integers.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">您還將獲得一個整數鍊錶的<code data-immersive-translate-walked="79cfcb01-19f4-44d7-931d-fe66a1ca65bd">head</code> 。</font></font></font></p>

<p data-immersive-translate-walked="79cfcb01-19f4-44d7-931d-fe66a1ca65bd" data-immersive-translate-paragraph="1">Generate an <code data-immersive-translate-walked="79cfcb01-19f4-44d7-931d-fe66a1ca65bd">m x n</code> matrix that contains the integers in the linked list presented in <strong data-immersive-translate-walked="79cfcb01-19f4-44d7-931d-fe66a1ca65bd">spiral</strong> order <strong data-immersive-translate-walked="79cfcb01-19f4-44d7-931d-fe66a1ca65bd">(clockwise)</strong>, starting from the <strong data-immersive-translate-walked="79cfcb01-19f4-44d7-931d-fe66a1ca65bd">top-left</strong> of the matrix. If there are remaining empty spaces, fill them with <code data-immersive-translate-walked="79cfcb01-19f4-44d7-931d-fe66a1ca65bd">-1</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">產生一個<code data-immersive-translate-walked="79cfcb01-19f4-44d7-931d-fe66a1ca65bd">mxn</code>矩陣，其中包含從矩陣<strong data-immersive-translate-walked="79cfcb01-19f4-44d7-931d-fe66a1ca65bd">左上角</strong>開始以<strong data-immersive-translate-walked="79cfcb01-19f4-44d7-931d-fe66a1ca65bd">螺旋</strong>順序<strong data-immersive-translate-walked="79cfcb01-19f4-44d7-931d-fe66a1ca65bd">（順時針）</strong>呈現的鍊錶中的整數。如果還有剩餘的空格，則用<code data-immersive-translate-walked="79cfcb01-19f4-44d7-931d-fe66a1ca65bd">-1</code>填滿它們。</font></font></font></p>

<p data-immersive-translate-walked="79cfcb01-19f4-44d7-931d-fe66a1ca65bd" data-immersive-translate-paragraph="1">Return <em data-immersive-translate-walked="79cfcb01-19f4-44d7-931d-fe66a1ca65bd">the generated matrix</em>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">傳回<em data-immersive-translate-walked="79cfcb01-19f4-44d7-931d-fe66a1ca65bd">生成的矩陣</em>。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/05/09/ex1new.jpg" style="width: 240px; height: 150px;">
<pre><strong>Input:</strong> m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
<strong>Output:</strong> [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
<strong>Explanation:</strong> The diagram above shows how the values are printed in the matrix.
Note that the remaining spaces in the matrix are filled with -1.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/05/11/ex2.jpg" style="width: 221px; height: 60px;">
<pre><strong>Input:</strong> m = 1, n = 4, head = [0,1,2]
<strong>Output:</strong> [[0,1,2,-1]]
<strong>Explanation:</strong> The diagram above shows how the values are printed from left to right in the matrix.
The last space in the matrix is set to -1.</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= m, n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li>The number of nodes in the list is in the range <code>[1, m * n]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 1000</code></li>
</ul>
</div>