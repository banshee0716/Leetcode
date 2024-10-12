<h2><a href="https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/">2406. Divide Intervals Into Minimum Number of Groups</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f" data-immersive-translate-paragraph="1">You are given a 2D integer array <code data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">intervals</code> where <code data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">intervals[i] = [left<sub>i</sub>, right<sub>i</sub>]</code> represents the <strong data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">inclusive</strong> interval <code data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">[left<sub>i</sub>, right<sub>i</sub>]</code>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個二維整數數組<code data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">intervals</code> ，其中 <code data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">intervals[i] = [left<sub>i</sub>, right<sub>i</sub>]</code> 表示<strong data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">包含</strong>區間<code data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">[left <sub>i</sub> , right <sub>i</sub> ]</code> 。</font></font></font></p>

<p data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f" data-immersive-translate-paragraph="1">You have to divide the intervals into one or more <strong data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">groups</strong> such that each interval is in <strong data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">exactly</strong> one group, and no two intervals that are in the same group <strong data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">intersect</strong> each other.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">您必須將間隔分為一組或多<strong data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">組，</strong>使得每個間隔<strong data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">恰好</strong>位於一組中，並且同一組中的兩個間隔不會彼此<strong data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">相交</strong>。</font></font></font></p>

<p data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f" data-immersive-translate-paragraph="1">Return <em data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">the <strong data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">minimum</strong> number of groups you need to make</em>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">傳回<em data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">您需要組成的<strong data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">最少</strong>組數</em>。</font></font></font></p>

<p data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f" data-immersive-translate-paragraph="1">Two intervals <strong data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">intersect</strong> if there is at least one common number between them. For example, the intervals <code data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">[1, 5]</code> and <code data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">[5, 8]</code> intersect.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">如果兩個區間之間至少有一個公共數，則它們<strong data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">相交</strong>。例如，區間<code data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">[1, 5]</code>和<code data-immersive-translate-walked="6354bee2-4f48-4bf9-af62-403b77f2314f">[5, 8]</code>相交。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> intervals = [[5,10],[6,8],[1,5],[2,3],[1,10]]
<strong>Output:</strong> 3
<strong>Explanation:</strong> We can divide the intervals into the following groups:
- Group 1: [1, 5], [6, 8].
- Group 2: [2, 3], [5, 10].
- Group 3: [1, 10].
It can be proven that it is not possible to divide the intervals into fewer than 3 groups.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> intervals = [[1,3],[5,6],[8,10],[11,13]]
<strong>Output:</strong> 1
<strong>Explanation:</strong> None of the intervals overlap, so we can put all of them in one group.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= intervals.length &lt;= 10<sup>5</sup></code></li>
	<li><code>intervals[i].length == 2</code></li>
	<li><code>1 &lt;= left<sub>i</sub> &lt;= right<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
</ul>
</div>