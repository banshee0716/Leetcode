<h2><a href="https://leetcode.com/problems/shortest-path-visiting-all-nodes/">847. Shortest Path Visiting All Nodes</a></h2><h3>Hard</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="83e2736c-001c-4b0d-8799-43094fd861c0">You have an undirected, connected graph of <code data-immersive-translate-effect="1" data-immersive_translate_walked="83e2736c-001c-4b0d-8799-43094fd861c0">n</code> nodes labeled from <code data-immersive-translate-effect="1" data-immersive_translate_walked="83e2736c-001c-4b0d-8799-43094fd861c0">0</code> to <code data-immersive-translate-effect="1" data-immersive_translate_walked="83e2736c-001c-4b0d-8799-43094fd861c0">n - 1</code>. You are given an array <code data-immersive-translate-effect="1" data-immersive_translate_walked="83e2736c-001c-4b0d-8799-43094fd861c0">graph</code> where <code data-immersive-translate-effect="1" data-immersive_translate_walked="83e2736c-001c-4b0d-8799-43094fd861c0">graph[i]</code> is a list of all the nodes connected with node <code data-immersive-translate-effect="1" data-immersive_translate_walked="83e2736c-001c-4b0d-8799-43094fd861c0">i</code> by an edge.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">您有一個標記為 to 的 <code data-immersive-translate-effect="1" data-immersive_translate_walked="83e2736c-001c-4b0d-8799-43094fd861c0">n</code>  <code data-immersive-translate-effect="1" data-immersive_translate_walked="83e2736c-001c-4b0d-8799-43094fd861c0">0</code> 無向連接節點圖 <code data-immersive-translate-effect="1" data-immersive_translate_walked="83e2736c-001c-4b0d-8799-43094fd861c0">n - 1</code> 。您將獲得一個陣列 <code data-immersive-translate-effect="1" data-immersive_translate_walked="83e2736c-001c-4b0d-8799-43094fd861c0">graph</code> ，其中 <code data-immersive-translate-effect="1" data-immersive_translate_walked="83e2736c-001c-4b0d-8799-43094fd861c0">graph[i]</code> 是通過邊與節點連接的所有節點 <code data-immersive-translate-effect="1" data-immersive_translate_walked="83e2736c-001c-4b0d-8799-43094fd861c0">i</code> 的清單。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="83e2736c-001c-4b0d-8799-43094fd861c0">Return <em data-immersive-translate-effect="1" data-immersive_translate_walked="83e2736c-001c-4b0d-8799-43094fd861c0">the length of the shortest path that visits every node</em>. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">返回訪問每個節點的最短路徑的長度。您可以在任何節點上啟動和停止，可以多次重新訪問節點，並且可以重用邊。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/12/shortest1-graph.jpg" style="width: 222px; height: 183px;">
<pre><strong>Input:</strong> graph = [[1,2,3],[0],[0],[0]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> One possible path is [1,0,2,0,3]
</pre>

<p><strong class="example">Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/12/shortest2-graph.jpg" style="width: 382px; height: 222px;">
<pre><strong>Input:</strong> graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> One possible path is [0,1,4,2,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == graph.length</code></li>
	<li><code>1 &lt;= n &lt;= 12</code></li>
	<li><code>0 &lt;= graph[i].length &lt;&nbsp;n</code></li>
	<li><code>graph[i]</code> does not contain <code>i</code>.</li>
	<li>If <code>graph[a]</code> contains <code>b</code>, then <code>graph[b]</code> contains <code>a</code>.</li>
	<li>The input graph is always connected.</li>
</ul>
</div>