<h2><a href="https://leetcode.com/problems/min-cost-to-connect-all-points/">1584. Min Cost to Connect All Points</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="2b63f73b-d7ef-44a6-a47c-095563f9e3f7">You are given an array <code data-immersive-translate-effect="1" data-immersive_translate_walked="2b63f73b-d7ef-44a6-a47c-095563f9e3f7">points</code> representing integer coordinates of some points on a 2D-plane, where <code data-immersive-translate-effect="1" data-immersive_translate_walked="2b63f73b-d7ef-44a6-a47c-095563f9e3f7">points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">您將取得 2D 平面上某些點的整數座標的陣列 <code data-immersive-translate-effect="1" data-immersive_translate_walked="2b63f73b-d7ef-44a6-a47c-095563f9e3f7">points</code> ，其中 <code data-immersive-translate-effect="1" data-immersive_translate_walked="2b63f73b-d7ef-44a6-a47c-095563f9e3f7">points[i] = [x<sub>i</sub>, y<sub>i</sub>]</code> .</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="2b63f73b-d7ef-44a6-a47c-095563f9e3f7">The cost of connecting two points <code data-immersive-translate-effect="1" data-immersive_translate_walked="2b63f73b-d7ef-44a6-a47c-095563f9e3f7">[x<sub>i</sub>, y<sub>i</sub>]</code> and <code data-immersive-translate-effect="1" data-immersive_translate_walked="2b63f73b-d7ef-44a6-a47c-095563f9e3f7">[x<sub>j</sub>, y<sub>j</sub>]</code> is the <strong data-immersive-translate-effect="1" data-immersive_translate_walked="2b63f73b-d7ef-44a6-a47c-095563f9e3f7">manhattan distance</strong> between them: <code data-immersive-translate-effect="1" data-immersive_translate_walked="2b63f73b-d7ef-44a6-a47c-095563f9e3f7">|x<sub>i</sub> - x<sub>j</sub>| + |y<sub>i</sub> - y<sub>j</sub>|</code>, where <code data-immersive-translate-effect="1" data-immersive_translate_walked="2b63f73b-d7ef-44a6-a47c-095563f9e3f7">|val|</code> denotes the absolute value of <code data-immersive-translate-effect="1" data-immersive_translate_walked="2b63f73b-d7ef-44a6-a47c-095563f9e3f7">val</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">連接兩點 <code data-immersive-translate-effect="1" data-immersive_translate_walked="2b63f73b-d7ef-44a6-a47c-095563f9e3f7">[x<sub>i</sub>, y<sub>i</sub>]</code> 的成本是 <code data-immersive-translate-effect="1" data-immersive_translate_walked="2b63f73b-d7ef-44a6-a47c-095563f9e3f7">[x<sub>j</sub>, y<sub>j</sub>]</code> 它們之間的曼哈頓距離： <code data-immersive-translate-effect="1" data-immersive_translate_walked="2b63f73b-d7ef-44a6-a47c-095563f9e3f7">|x<sub>i</sub> - x<sub>j</sub>| + |y<sub>i</sub> - y<sub>j</sub>|</code> ，其中 <code data-immersive-translate-effect="1" data-immersive_translate_walked="2b63f73b-d7ef-44a6-a47c-095563f9e3f7">|val|</code> 表示 的 <code data-immersive-translate-effect="1" data-immersive_translate_walked="2b63f73b-d7ef-44a6-a47c-095563f9e3f7">val</code> 絕對值。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="2b63f73b-d7ef-44a6-a47c-095563f9e3f7">Return <em data-immersive-translate-effect="1" data-immersive_translate_walked="2b63f73b-d7ef-44a6-a47c-095563f9e3f7">the minimum cost to make all points connected.</em> All points are connected if there is <strong data-immersive-translate-effect="1" data-immersive_translate_walked="2b63f73b-d7ef-44a6-a47c-095563f9e3f7">exactly one</strong> simple path between any two points.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">返回使所有點連接的最低成本。如果任意兩點之間只有一條簡單路徑，則所有點都連接在一起。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/26/d.png" style="width: 214px; height: 268px;">
<pre><strong>Input:</strong> points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
<strong>Output:</strong> 20
<strong>Explanation:</strong> 
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/26/c.png" style="width: 214px; height: 268px;">
We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> points = [[3,12],[-2,5],[-4,1]]
<strong>Output:</strong> 18
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= points.length &lt;= 1000</code></li>
	<li><code>-10<sup>6</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 10<sup>6</sup></code></li>
	<li>All pairs <code>(x<sub>i</sub>, y<sub>i</sub>)</code> are distinct.</li>
</ul>
</div>