<h2><a href="https://leetcode.com/problems/special-positions-in-a-binary-matrix/">1582. Special Positions in a Binary Matrix</a></h2><h3>Easy</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="3e4deeb4-3d9d-40dc-b00f-39683ef2f9a3">Given an <code data-immersive-translate-effect="1" data-immersive_translate_walked="3e4deeb4-3d9d-40dc-b00f-39683ef2f9a3">m x n</code> binary matrix <code data-immersive-translate-effect="1" data-immersive_translate_walked="3e4deeb4-3d9d-40dc-b00f-39683ef2f9a3">mat</code>, return <em data-immersive-translate-effect="1" data-immersive_translate_walked="3e4deeb4-3d9d-40dc-b00f-39683ef2f9a3">the number of special positions in </em><code data-immersive-translate-effect="1" data-immersive_translate_walked="3e4deeb4-3d9d-40dc-b00f-39683ef2f9a3">mat</code><font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個 <code data-immersive-translate-effect="1" data-immersive_translate_walked="3e4deeb4-3d9d-40dc-b00f-39683ef2f9a3">m x n</code> 二元矩陣 <code data-immersive-translate-effect="1" data-immersive_translate_walked="3e4deeb4-3d9d-40dc-b00f-39683ef2f9a3">mat</code> ，返回 <code data-immersive-translate-effect="1" data-immersive_translate_walked="3e4deeb4-3d9d-40dc-b00f-39683ef2f9a3">mat</code> </font></font></font><em>.</em></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="3e4deeb4-3d9d-40dc-b00f-39683ef2f9a3">A position <code data-immersive-translate-effect="1" data-immersive_translate_walked="3e4deeb4-3d9d-40dc-b00f-39683ef2f9a3">(i, j)</code> is called <strong data-immersive-translate-effect="1" data-immersive_translate_walked="3e4deeb4-3d9d-40dc-b00f-39683ef2f9a3">special</strong> if <code data-immersive-translate-effect="1" data-immersive_translate_walked="3e4deeb4-3d9d-40dc-b00f-39683ef2f9a3">mat[i][j] == 1</code> and all other elements in row <code data-immersive-translate-effect="1" data-immersive_translate_walked="3e4deeb4-3d9d-40dc-b00f-39683ef2f9a3">i</code> and column <code data-immersive-translate-effect="1" data-immersive_translate_walked="3e4deeb4-3d9d-40dc-b00f-39683ef2f9a3">j</code> are <code data-immersive-translate-effect="1" data-immersive_translate_walked="3e4deeb4-3d9d-40dc-b00f-39683ef2f9a3">0</code> (rows and columns are <strong data-immersive-translate-effect="1" data-immersive_translate_walked="3e4deeb4-3d9d-40dc-b00f-39683ef2f9a3">0-indexed</strong>).<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">如果 <code data-immersive-translate-effect="1" data-immersive_translate_walked="3e4deeb4-3d9d-40dc-b00f-39683ef2f9a3">mat[i][j] == 1</code> 且行 <code data-immersive-translate-effect="1" data-immersive_translate_walked="3e4deeb4-3d9d-40dc-b00f-39683ef2f9a3">i</code> 和列 <code data-immersive-translate-effect="1" data-immersive_translate_walked="3e4deeb4-3d9d-40dc-b00f-39683ef2f9a3">j</code> 中的所有其他元素都為 （行和列的索引為 <code data-immersive-translate-effect="1" data-immersive_translate_walked="3e4deeb4-3d9d-40dc-b00f-39683ef2f9a3">0</code> 0），則位置稱為特殊位置 <code data-immersive-translate-effect="1" data-immersive_translate_walked="3e4deeb4-3d9d-40dc-b00f-39683ef2f9a3">(i, j)</code> 。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/23/special1.jpg" style="width: 244px; height: 245px;">
<pre><strong>Input:</strong> mat = [[1,0,0],[0,0,1],[1,0,0]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> (1, 2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/24/special-grid.jpg" style="width: 244px; height: 245px;">
<pre><strong>Input:</strong> mat = [[1,0,0],[0,1,0],[0,0,1]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> (0, 0), (1, 1) and (2, 2) are special positions.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 100</code></li>
	<li><code>mat[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>
</div>