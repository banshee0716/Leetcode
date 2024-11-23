<h2><a href="https://leetcode.com/problems/rotating-the-box/">1861. Rotating the Box</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e" data-immersive-translate-paragraph="1">You are given an <code data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e">m x n</code> matrix of characters <code data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e">box</code> representing a side-view of a box. Each cell of the box is one of the following:<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定一個<code data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e">mxn</code>字元<code data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e">box</code>矩陣，表示盒子的側視圖。盒子的每個單元格都是以下之一：</font></font></font></p>

<ul>
	<li>A stone <code>'#'</code></li>
	<li>A stationary obstacle <code>'*'</code></li>
	<li>Empty <code>'.'</code></li>
</ul>

<p data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e" data-immersive-translate-paragraph="1">The box is rotated <strong data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e">90 degrees clockwise</strong>, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity <strong data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e">does not</strong> affect the obstacles' positions, and the inertia from the box's rotation <strong data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e">does not </strong>affect the stones' horizontal positions.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">盒子<strong data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e">順時針旋轉90度</strong>，導致一些石頭因重力而掉落。每塊石頭都會下落，直到落在障礙物、另一塊石頭或箱子的底部。重力<strong data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e">不會</strong>影響障礙物的位置，盒子旋轉的慣性<strong data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e">也不會</strong>影響石頭的水平位置。</font></font></font></p>

<p data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e" data-immersive-translate-paragraph="1">It is <strong data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e">guaranteed</strong> that each stone in <code data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e">box</code> rests on an obstacle, another stone, or the bottom of the box.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"><strong data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e">確保</strong><code data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e">box</code>中的每塊石頭都放置在障礙物、另一塊石頭或盒子的底部。</font></font></font></p>

<p data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e" data-immersive-translate-paragraph="1">Return <em data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e">an </em><code data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e">n x m</code><em data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e"> matrix representing the box after the rotation described above</em>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">傳回<em data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e">一個</em><code data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e">nxm</code><em data-immersive-translate-walked="41f0a81c-df7e-4f80-a0fd-461911fff40e">矩陣，表示經過上述旋轉後的框框</em>。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcodewithstones.png" style="width: 300px; height: 150px;"></p>

<pre><strong>Input:</strong> box = [["#",".","#"]]
<strong>Output:</strong> [["."],
&nbsp;        ["#"],
&nbsp;        ["#"]]
</pre>

<p><strong class="example">Example 2:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode2withstones.png" style="width: 375px; height: 195px;"></p>

<pre><strong>Input:</strong> box = [["#",".","*","."],
&nbsp;             ["#","#","*","."]]
<strong>Output:</strong> [["#","."],
&nbsp;        ["#","#"],
&nbsp;        ["*","*"],
&nbsp;        [".","."]]
</pre>

<p><strong class="example">Example 3:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode3withstone.png" style="width: 400px; height: 218px;"></p>

<pre><strong>Input:</strong> box = [["#","#","*",".","*","."],
&nbsp;             ["#","#","#","*",".","."],
&nbsp;             ["#","#","#",".","#","."]]
<strong>Output:</strong> [[".","#","#"],
&nbsp;        [".","#","#"],
&nbsp;        ["#","#","*"],
&nbsp;        ["#","*","."],
&nbsp;        ["#",".","*"],
&nbsp;        ["#",".","."]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>m == box.length</code></li>
	<li><code>n == box[i].length</code></li>
	<li><code>1 &lt;= m, n &lt;= 500</code></li>
	<li><code>box[i][j]</code> is either <code>'#'</code>, <code>'*'</code>, or <code>'.'</code>.</li>
</ul></div>