<h2><a href="https://leetcode.com/problems/walking-robot-simulation/">874. Walking Robot Simulation</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517" data-immersive-translate-paragraph="1">A robot on an infinite XY-plane starts at point <code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">(0, 0)</code> facing north. The robot can receive a sequence of these three possible types of <code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">commands</code>:<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">無限 XY 平面上的機器人從面向北的點<code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">(0, 0)</code>開始。機器人可以接收這三種可能類型的<code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">commands</code>的序列：</font></font></font></p>

<ul>
	<li data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517" data-immersive-translate-paragraph="1"><code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">-2</code>: Turn left <code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">90</code> degrees.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"><code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">-2</code> ：左轉<code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">90</code>度。</font></font></font></li>
	<li data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517" data-immersive-translate-paragraph="1"><code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">-1</code>: Turn right <code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">90</code> degrees.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"><code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">-1</code> ：右轉<code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">90</code>度。</font></font></font></li>
	<li data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517" data-immersive-translate-paragraph="1"><code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">1 &lt;= k &lt;= 9</code>: Move forward <code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">k</code> units, one unit at a time.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"><code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">1 &lt;= k &lt;= 9</code> ：向前移動<code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">k</code>單位，一次一個單位。</font></font></font></li>
</ul>

<p data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517" data-immersive-translate-paragraph="1">Some of the grid squares are <code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">obstacles</code>. The <code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">i<sup>th</sup></code> obstacle is at grid point <code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">obstacles[i] = (x<sub>i</sub>, y<sub>i</sub>)</code>. If the robot runs into an obstacle, then it will instead stay in its current location and move on to the next command.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">有些網格方塊是<code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">obstacles</code> 。 <code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">i <sup>th</sup></code>障礙物位於網格點<code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">obstacles[i] = (x <sub>i</sub> , y <sub>i</sub> )</code>處。如果機器人遇到障礙物，那麼它將留在當前位置並繼續執行下一個命令。</font></font></font></p>

<p data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517" data-immersive-translate-paragraph="1">Return <em data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">the <strong data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">maximum Euclidean distance</strong> that the robot ever gets from the origin <strong data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">squared</strong> (i.e. if the distance is </em><code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">5</code><em data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">, return </em><code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">25</code><em data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">)</em>.<font class="notranslate immersive-translate-target-wrapper" data-immersive-translate-translation-element-mark="1" lang="zh-TW"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">返回<em data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">機器人從<strong data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">原點</strong>得到的<strong data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">最大歐幾里德距離</strong>的平方（即，如果距離為</em><code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">5</code> <em data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">，則返回</em><code data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">25</code> <em data-immersive-translate-walked="54e84668-de85-4a43-bbac-3e7e088b6517">）</em> 。</font></font></font></p>

<p><strong>Note:</strong></p>

<ul>
	<li>North means +Y direction.</li>
	<li>East means +X direction.</li>
	<li>South means -Y direction.</li>
	<li>West means -X direction.</li>
	<li>There can be obstacle in&nbsp;[0,0].</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> commands = [4,-1,3], obstacles = []
<strong>Output:</strong> 25
<strong>Explanation:</strong> The robot starts at (0, 0):
1. Move north 4 units to (0, 4).
2. Turn right.
3. Move east 3 units to (3, 4).
The furthest point the robot ever gets from the origin is (3, 4), which squared is 3<sup>2</sup> + 4<sup>2</sup> = 25 units away.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> commands = [4,-1,4,-2,4], obstacles = [[2,4]]
<strong>Output:</strong> 65
<strong>Explanation:</strong> The robot starts at (0, 0):
1. Move north 4 units to (0, 4).
2. Turn right.
3. Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at (1, 4).
4. Turn left.
5. Move north 4 units to (1, 8).
The furthest point the robot ever gets from the origin is (1, 8), which squared is 1<sup>2</sup> + 8<sup>2</sup> = 65 units away.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> commands = [6,-1,-1,6], obstacles = []
<strong>Output:</strong> 36
<strong>Explanation:</strong> The robot starts at (0, 0):
1. Move north 6 units to (0, 6).
2. Turn right.
3. Turn right.
4. Move south 6 units to (0, 0).
The furthest point the robot ever gets from the origin is (0, 6), which squared is 6<sup>2</sup> = 36 units away.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= commands.length &lt;= 10<sup>4</sup></code></li>
	<li><code>commands[i]</code> is either <code>-2</code>, <code>-1</code>, or an integer in the range <code>[1, 9]</code>.</li>
	<li><code>0 &lt;= obstacles.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-3 * 10<sup>4</sup> &lt;= x<sub>i</sub>, y<sub>i</sub> &lt;= 3 * 10<sup>4</sup></code></li>
	<li>The answer is guaranteed to be less than <code>2<sup>31</sup></code>.</li>
</ul>
</div>