<h2><a href="https://leetcode.com/problems/linked-list-cycle/">141. Linked List Cycle</a></h2><h3>Easy</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="c8fef3bf-3228-4454-973d-df7a35ebaef7">Given <code data-immersive-translate-effect="1" data-immersive_translate_walked="c8fef3bf-3228-4454-973d-df7a35ebaef7">head</code>, the head of a linked list, determine if the linked list has a cycle in it.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定 <code data-immersive-translate-effect="1" data-immersive_translate_walked="c8fef3bf-3228-4454-973d-df7a35ebaef7">head</code> 鏈表的頭部，確定鏈表是否有迴圈。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="c8fef3bf-3228-4454-973d-df7a35ebaef7">There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the&nbsp;<code data-immersive-translate-effect="1" data-immersive_translate_walked="c8fef3bf-3228-4454-973d-df7a35ebaef7">next</code>&nbsp;pointer. Internally, <code data-immersive-translate-effect="1" data-immersive_translate_walked="c8fef3bf-3228-4454-973d-df7a35ebaef7">pos</code>&nbsp;is used to denote the index of the node that&nbsp;tail's&nbsp;<code data-immersive-translate-effect="1" data-immersive_translate_walked="c8fef3bf-3228-4454-973d-df7a35ebaef7">next</code>&nbsp;pointer is connected to.&nbsp;<strong data-immersive-translate-effect="1" data-immersive_translate_walked="c8fef3bf-3228-4454-973d-df7a35ebaef7">Note that&nbsp;<code data-immersive-translate-effect="1" data-immersive_translate_walked="c8fef3bf-3228-4454-973d-df7a35ebaef7">pos</code>&nbsp;is not passed as a parameter</strong>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">如果清單中存在某個節點，可以通過連續跟隨 <code data-immersive-translate-effect="1" data-immersive_translate_walked="c8fef3bf-3228-4454-973d-df7a35ebaef7">next</code> 指標再次到達，則鏈表中存在一個迴圈。在內部， <code data-immersive-translate-effect="1" data-immersive_translate_walked="c8fef3bf-3228-4454-973d-df7a35ebaef7">pos</code> 用於表示尾部 <code data-immersive-translate-effect="1" data-immersive_translate_walked="c8fef3bf-3228-4454-973d-df7a35ebaef7">next</code> 指標連接到的節點的索引。請注意，它 <code data-immersive-translate-effect="1" data-immersive_translate_walked="c8fef3bf-3228-4454-973d-df7a35ebaef7">pos</code> 不會作為參數傳遞。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="c8fef3bf-3228-4454-973d-df7a35ebaef7">Return&nbsp;<code data-immersive-translate-effect="1" data-immersive_translate_walked="c8fef3bf-3228-4454-973d-df7a35ebaef7">true</code><em data-immersive-translate-effect="1" data-immersive_translate_walked="c8fef3bf-3228-4454-973d-df7a35ebaef7"> if there is a cycle in the linked list</em>. Otherwise, return <code data-immersive-translate-effect="1" data-immersive_translate_walked="c8fef3bf-3228-4454-973d-df7a35ebaef7">false</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">如果鏈表中有迴圈，則返回 <code data-immersive-translate-effect="1" data-immersive_translate_walked="c8fef3bf-3228-4454-973d-df7a35ebaef7">true</code> 。否則，返回 <code data-immersive-translate-effect="1" data-immersive_translate_walked="c8fef3bf-3228-4454-973d-df7a35ebaef7">false</code> 。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png" style="width: 300px; height: 97px; margin-top: 8px; margin-bottom: 8px;">
<pre><strong>Input:</strong> head = [3,2,0,-4], pos = 1
<strong>Output:</strong> true
<strong>Explanation:</strong> There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test2.png" style="width: 141px; height: 74px;">
<pre><strong>Input:</strong> head = [1,2], pos = 0
<strong>Output:</strong> true
<strong>Explanation:</strong> There is a cycle in the linked list, where the tail connects to the 0th node.
</pre>

<p><strong class="example">Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist_test3.png" style="width: 45px; height: 45px;">
<pre><strong>Input:</strong> head = [1], pos = -1
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no cycle in the linked list.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of the nodes in the list is in the range <code>[0, 10<sup>4</sup>]</code>.</li>
	<li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li><code>pos</code> is <code>-1</code> or a <strong>valid index</strong> in the linked-list.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Can you solve it using <code>O(1)</code> (i.e. constant) memory?</p>
</div>