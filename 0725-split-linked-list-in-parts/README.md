<h2><a href="https://leetcode.com/problems/split-linked-list-in-parts/">725. Split Linked List in Parts</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="49683510-d1e9-4f12-ac89-b6425f0e03b4">Given the <code data-immersive-translate-effect="1" data-immersive_translate_walked="49683510-d1e9-4f12-ac89-b6425f0e03b4">head</code> of a singly linked list and an integer <code data-immersive-translate-effect="1" data-immersive_translate_walked="49683510-d1e9-4f12-ac89-b6425f0e03b4">k</code>, split the linked list into <code data-immersive-translate-effect="1" data-immersive_translate_walked="49683510-d1e9-4f12-ac89-b6425f0e03b4">k</code> consecutive linked list parts.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"> <code data-immersive-translate-effect="1" data-immersive_translate_walked="49683510-d1e9-4f12-ac89-b6425f0e03b4">head</code> 給定一個單向鏈表和一個整數 <code data-immersive-translate-effect="1" data-immersive_translate_walked="49683510-d1e9-4f12-ac89-b6425f0e03b4">k</code> ，將鏈表拆分為 <code data-immersive-translate-effect="1" data-immersive_translate_walked="49683510-d1e9-4f12-ac89-b6425f0e03b4">k</code> 連續的鏈表部分。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="49683510-d1e9-4f12-ac89-b6425f0e03b4">The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">每個零件的長度應盡可能相等：任何兩個零件的尺寸都不應相差超過一個。這可能會導致某些部分為空。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="49683510-d1e9-4f12-ac89-b6425f0e03b4">The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">部件應按輸入清單中的出現順序排列，較早出現的部件的大小應始終大於或等於較晚出現的部件。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="49683510-d1e9-4f12-ac89-b6425f0e03b4">Return <em data-immersive-translate-effect="1" data-immersive_translate_walked="49683510-d1e9-4f12-ac89-b6425f0e03b4">an array of the </em><code data-immersive-translate-effect="1" data-immersive_translate_walked="49683510-d1e9-4f12-ac89-b6425f0e03b4">k</code><em data-immersive-translate-effect="1" data-immersive_translate_walked="49683510-d1e9-4f12-ac89-b6425f0e03b4"> parts</em>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">返回 <code data-immersive-translate-effect="1" data-immersive_translate_walked="49683510-d1e9-4f12-ac89-b6425f0e03b4">k</code> 部件的陣列。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/13/split1-lc.jpg" style="width: 400px; height: 134px;">
<pre><strong>Input:</strong> head = [1,2,3], k = 5
<strong>Output:</strong> [[1],[2],[3],[],[]]
<strong>Explanation:</strong>
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/13/split2-lc.jpg" style="width: 600px; height: 60px;">
<pre><strong>Input:</strong> head = [1,2,3,4,5,6,7,8,9,10], k = 3
<strong>Output:</strong> [[1,2,3,4],[5,6,7],[8,9,10]]
<strong>Explanation:</strong>
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[0, 1000]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 1000</code></li>
	<li><code>1 &lt;= k &lt;= 50</code></li>
</ul>
</div>