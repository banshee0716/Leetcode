<h2><a href="https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/">1337. The K Weakest Rows in a Matrix</a></h2><h3>Easy</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">You are given an <code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">m x n</code> binary matrix <code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">mat</code> of <code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">1</code>'s (representing soldiers) and <code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">0</code>'s (representing civilians). The soldiers are positioned <strong data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">in front</strong> of the civilians. That is, all the <code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">1</code>'s will appear to the <strong data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">left</strong> of all the <code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">0</code>'s in each row.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">您將獲得 『（代表士兵）和 『（代表平民）的 <code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">m x n</code> <code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">1</code> 二進位矩陣 <code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">mat</code> 。 <code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">0</code> 士兵們站在平民面前。也就是說，所有的 都將顯示在每行中所有 <code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">1</code> <code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">0</code> 的左側。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">A row <code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">i</code> is <strong data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">weaker</strong> than a row <code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">j</code> if one of the following is true:<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">如果滿足以下條件之一，則行比行 <code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">i</code>  <code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">j</code> 弱：</font></font></font></p>

<ul>
	<li data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">The number of soldiers in row <code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">i</code> is less than the number of soldiers in row <code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">j</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">排兵人數少於排 <code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">i</code> <code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">j</code> 兵人數.</font></font></font></li>
	<li data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">Both rows have the same number of soldiers and <code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">i &lt; j</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">兩行具有相同數量的士兵和 <code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">i &lt; j</code> .</font></font></font></li>
</ul>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">Return <em data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">the indices of the </em><code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">k</code><em data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877"> <strong data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">weakest</strong> rows in the matrix ordered from weakest to strongest</em>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">返回矩陣中最弱行 <code data-immersive-translate-effect="1" data-immersive_translate_walked="46ad430e-7138-4562-9aca-d9fc45045877">k</code> 的索引，按從最弱到最強的順序排列。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
<strong>Output:</strong> [2,0,3]
<strong>Explanation:</strong> 
The number of soldiers in each row is: 
- Row 0: 2 
- Row 1: 4 
- Row 2: 1 
- Row 3: 2 
- Row 4: 5 
The rows ordered from weakest to strongest are [2,0,3,1,4].
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
<strong>Output:</strong> [0,2]
<strong>Explanation:</strong> 
The number of soldiers in each row is: 
- Row 0: 1 
- Row 1: 4 
- Row 2: 1 
- Row 3: 1 
The rows ordered from weakest to strongest are [0,2,3,1].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == mat.length</code></li>
	<li><code>n == mat[i].length</code></li>
	<li><code>2 &lt;= n, m &lt;= 100</code></li>
	<li><code>1 &lt;= k &lt;= m</code></li>
	<li><code>matrix[i][j]</code> is either 0 or 1.</li>
</ul>
</div>