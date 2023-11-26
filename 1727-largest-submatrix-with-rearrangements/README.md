<h2><a href="https://leetcode.com/problems/largest-submatrix-with-rearrangements/">1727. Largest Submatrix With Rearrangements</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="5168631c-bfea-479b-8de0-02b8adb31215">You are given a binary matrix <code data-immersive-translate-effect="1" data-immersive_translate_walked="5168631c-bfea-479b-8de0-02b8adb31215">matrix</code> of size <code data-immersive-translate-effect="1" data-immersive_translate_walked="5168631c-bfea-479b-8de0-02b8adb31215">m x n</code>, and you are allowed to rearrange the <strong data-immersive-translate-effect="1" data-immersive_translate_walked="5168631c-bfea-479b-8de0-02b8adb31215">columns</strong> of the <code data-immersive-translate-effect="1" data-immersive_translate_walked="5168631c-bfea-479b-8de0-02b8adb31215">matrix</code> in any order.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">你得到一個大小 <code data-immersive-translate-effect="1" data-immersive_translate_walked="5168631c-bfea-479b-8de0-02b8adb31215">m x n</code> 的二進位矩陣，你可以以任何順序重新排列 <code data-immersive-translate-effect="1" data-immersive_translate_walked="5168631c-bfea-479b-8de0-02b8adb31215">matrix</code> 的 <code data-immersive-translate-effect="1" data-immersive_translate_walked="5168631c-bfea-479b-8de0-02b8adb31215">matrix</code> 列。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="5168631c-bfea-479b-8de0-02b8adb31215">Return <em data-immersive-translate-effect="1" data-immersive_translate_walked="5168631c-bfea-479b-8de0-02b8adb31215">the area of the largest submatrix within </em><code data-immersive-translate-effect="1" data-immersive_translate_walked="5168631c-bfea-479b-8de0-02b8adb31215">matrix</code><em data-immersive-translate-effect="1" data-immersive_translate_walked="5168631c-bfea-479b-8de0-02b8adb31215"> where <strong data-immersive-translate-effect="1" data-immersive_translate_walked="5168631c-bfea-479b-8de0-02b8adb31215">every</strong> element of the submatrix is </em><code data-immersive-translate-effect="1" data-immersive_translate_walked="5168631c-bfea-479b-8de0-02b8adb31215">1</code><em data-immersive-translate-effect="1" data-immersive_translate_walked="5168631c-bfea-479b-8de0-02b8adb31215"> after reordering the columns optimally.</em><font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">在對列進行最佳重新排序后，返回最大子矩陣的面積， <code data-immersive-translate-effect="1" data-immersive_translate_walked="5168631c-bfea-479b-8de0-02b8adb31215">matrix</code> 其中每個元素所在的 <code data-immersive-translate-effect="1" data-immersive_translate_walked="5168631c-bfea-479b-8de0-02b8adb31215">1</code> 位置。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/29/screenshot-2020-12-30-at-40536-pm.png" style="width: 500px; height: 240px;">
<pre><strong>Input:</strong> matrix = [[0,0,1],[1,1,1],[1,0,1]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 4.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/29/screenshot-2020-12-30-at-40852-pm.png" style="width: 500px; height: 62px;">
<pre><strong>Input:</strong> matrix = [[1,0,1,0,1]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> You can rearrange the columns as shown above.
The largest submatrix of 1s, in bold, has an area of 3.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> matrix = [[1,1,0],[1,0,1]]
<strong>Output:</strong> 2
<strong>Explanation:</strong> Notice that you must rearrange entire columns, and there is no way to make a submatrix of 1s larger than an area of 2.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == matrix.length</code></li>
	<li><code>n == matrix[i].length</code></li>
	<li><code>1 &lt;= m * n &lt;= 10<sup>5</sup></code></li>
	<li><code>matrix[i][j]</code> is either <code>0</code> or <code>1</code>.</li>
</ul>
</div>