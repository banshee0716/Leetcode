<h2><a href="https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/">3217. Delete Nodes From Linked List Present in Array<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">3217. 從陣列中存在的鍊錶中刪除節點</font></font></font></a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="dbddb779-b2b1-416f-bc46-8afc21ef11e6" data-immersive-translate-paragraph="1">You are given an array of integers <code data-immersive-translate-walked="dbddb779-b2b1-416f-bc46-8afc21ef11e6">nums</code> and the <code data-immersive-translate-walked="dbddb779-b2b1-416f-bc46-8afc21ef11e6">head</code> of a linked list. Return the <code data-immersive-translate-walked="dbddb779-b2b1-416f-bc46-8afc21ef11e6">head</code> of the modified linked list after <strong data-immersive-translate-walked="dbddb779-b2b1-416f-bc46-8afc21ef11e6">removing</strong> all nodes from the linked list that have a value that exists in <code data-immersive-translate-walked="dbddb779-b2b1-416f-bc46-8afc21ef11e6">nums</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個整數數組<code data-immersive-translate-walked="dbddb779-b2b1-416f-bc46-8afc21ef11e6">nums</code>和一個鍊錶的<code data-immersive-translate-walked="dbddb779-b2b1-416f-bc46-8afc21ef11e6">head</code> 。從鍊錶中<strong data-immersive-translate-walked="dbddb779-b2b1-416f-bc46-8afc21ef11e6">刪除</strong>具有<code data-immersive-translate-walked="dbddb779-b2b1-416f-bc46-8afc21ef11e6">nums</code>中存在的值的所有節點後，返回修改後的鍊錶的<code data-immersive-translate-walked="dbddb779-b2b1-416f-bc46-8afc21ef11e6">head</code> 。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1,2,3], head = [1,2,3,4,5]</span></p>

<p><strong>Output:</strong> <span class="example-io">[4,5]</span></p>

<p><strong>Explanation:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample0.png" style="width: 400px; height: 66px;"></strong></p>

<p>Remove the nodes with values 1, 2, and 3.</p>
</div>

<p><strong class="example">Example 2:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [1], head = [1,2,1,2,1,2]</span></p>

<p><strong>Output:</strong> <span class="example-io">[2,2,2]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample1.png" style="height: 62px; width: 450px;"></p>

<p>Remove the nodes with value 1.</p>
</div>

<p><strong class="example">Example 3:</strong></p>

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">nums = [5], head = [1,2,3,4]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,2,3,4]</span></p>

<p><strong>Explanation:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2024/06/11/linkedlistexample2.png" style="width: 400px; height: 83px;"></strong></p>

<p>No node has value 5.</p>
</div>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
	<li>All elements in <code>nums</code> are unique.</li>
	<li>The number of nodes in the given list is in the range <code>[1, 10<sup>5</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 10<sup>5</sup></code></li>
	<li>The input is generated such that there is at least one node in the linked list that has a value not present in <code>nums</code>.</li>
</ul>
</div>