<h2><a href="https://leetcode.com/problems/linked-list-in-binary-tree/">1367. Linked List in Binary Tree</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="28afe6a7-8ce4-44c8-a704-4fdc7b250771" data-immersive-translate-paragraph="1">Given a binary tree <code data-immersive-translate-walked="28afe6a7-8ce4-44c8-a704-4fdc7b250771">root</code> and a&nbsp;linked list with&nbsp;<code data-immersive-translate-walked="28afe6a7-8ce4-44c8-a704-4fdc7b250771">head</code>&nbsp;as the first node.&nbsp;<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個二元<code data-immersive-translate-walked="28afe6a7-8ce4-44c8-a704-4fdc7b250771">root</code>和一個<code data-immersive-translate-walked="28afe6a7-8ce4-44c8-a704-4fdc7b250771">head</code>為第一個節點的鍊錶。</font></font></font></p>

<p data-immersive-translate-walked="28afe6a7-8ce4-44c8-a704-4fdc7b250771" data-immersive-translate-paragraph="1">Return True if all the elements in the linked list starting from the <code data-immersive-translate-walked="28afe6a7-8ce4-44c8-a704-4fdc7b250771">head</code> correspond to some <em data-immersive-translate-walked="28afe6a7-8ce4-44c8-a704-4fdc7b250771">downward path</em> connected in the binary tree&nbsp;otherwise return False.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">如果鍊錶中<code data-immersive-translate-walked="28afe6a7-8ce4-44c8-a704-4fdc7b250771">head</code>開始的所有元素都對應於二元樹中連接的某個<em data-immersive-translate-walked="28afe6a7-8ce4-44c8-a704-4fdc7b250771">向下路徑</em>，則傳回 True，否則傳回 False。</font></font></font></p>

<p data-immersive-translate-walked="28afe6a7-8ce4-44c8-a704-4fdc7b250771" data-immersive-translate-paragraph="1">In this context downward path means a path that starts at some node and goes downwards.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">在這種情況下，向下路徑意味著從某個節點開始並向下的路徑。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2020/02/12/sample_1_1720.png" style="width: 220px; height: 280px;"></strong></p>

<pre><strong>Input:</strong> head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
<strong>Output:</strong> true
<strong>Explanation:</strong> Nodes in blue form a subpath in the binary Tree.  
</pre>

<p><strong class="example">Example 2:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2020/02/12/sample_2_1720.png" style="width: 220px; height: 280px;"></strong></p>

<pre><strong>Input:</strong> head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
<strong>Output:</strong> true
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
<strong>Output:</strong> false
<strong>Explanation:</strong> There is no path in the binary tree that contains all the elements of the linked list from <code>head</code>.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree will be in the range <code>[1, 2500]</code>.</li>
	<li>The number of nodes in the list will be in the range <code>[1, 100]</code>.</li>
	<li><code>1 &lt;= Node.val&nbsp;&lt;= 100</code>&nbsp;for each node in the linked list and binary tree.</li>
</ul>
</div>