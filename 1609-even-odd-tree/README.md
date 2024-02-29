<h2><a href="https://leetcode.com/problems/even-odd-tree/">1609. Even Odd Tree</a></h2><h3>Medium</h3><hr><div><p>A binary tree is named <strong>Even-Odd</strong> if it meets the following conditions:</p>

<ul>
	<li data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1" data-immersive-translate-paragraph="1">The root of the binary tree is at level index <code data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1">0</code>, its children are at level index <code data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1">1</code>, their children are at level index <code data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1">2</code>, etc.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">二叉樹的根在水準索引，它的子樹在水準索引，它們的子樹在水準索引 <code data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1">0</code> <code data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1">1</code> <code data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1">2</code> ，等等。</font></font></font></li>
	<li data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1" data-immersive-translate-paragraph="1">For every <strong data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1">even-indexed</strong> level, all nodes at the level have <strong data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1">odd</strong> integer values in <strong data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1">strictly increasing</strong> order (from left to right).<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">對於每個偶數索引級別，該級別的所有節點都具有嚴格遞增的奇數整數值（從左到右）。</font></font></font></li>
	<li data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1" data-immersive-translate-paragraph="1">For every <b data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1">odd-indexed</b> level, all nodes at the level have <b data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1">even</b> integer values in <strong data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1">strictly decreasing</strong> order (from left to right).<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">對於每個奇數索引級別，該級別的所有節點都具有嚴格降序（從左到右）的偶數整數值。</font></font></font></li>
</ul>

<p data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1" data-immersive-translate-paragraph="1">Given the <code data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1">root</code> of a binary tree, <em data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1">return </em><code data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1">true</code><em data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1"> if the binary tree is <strong data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1">Even-Odd</strong>, otherwise return </em><code data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1">false</code><font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定二叉樹 <code data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1">root</code> ，如果二叉樹為偶奇數，則返回，否則返回 <code data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1">true</code> <code data-immersive-translate-walked="300f0b01-2dc4-4a4a-9963-6b3a1a7025f1">false</code> </font></font></font><em>.</em></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/sample_1_1966.png" style="width: 362px; height: 229px;">
<pre><strong>Input:</strong> root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
<strong>Output:</strong> true
<strong>Explanation:</strong> The node values on each level are:
Level 0: [1]
Level 1: [10,4]
Level 2: [3,7,9]
Level 3: [12,8,6,2]
Since levels 0 and 2 are all odd and increasing and levels 1 and 3 are all even and decreasing, the tree is Even-Odd.
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/sample_2_1966.png" style="width: 363px; height: 167px;">
<pre><strong>Input:</strong> root = [5,4,2,3,3,7]
<strong>Output:</strong> false
<strong>Explanation:</strong> The node values on each level are:
Level 0: [5]
Level 1: [4,2]
Level 2: [3,3,7]
Node values in level 2 must be in strictly increasing order, so the tree is not Even-Odd.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/22/sample_1_333_1966.png" style="width: 363px; height: 167px;">
<pre><strong>Input:</strong> root = [5,9,1,3,5,7]
<strong>Output:</strong> false
<strong>Explanation:</strong> Node values in the level 1 should be even integers.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 10<sup>5</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>6</sup></code></li>
</ul>
</div>