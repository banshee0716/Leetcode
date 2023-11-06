<h2><a href="https://leetcode.com/problems/seat-reservation-manager/">1845. Seat Reservation Manager</a></h2><h3>Medium</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">Design a system that manages the reservation state of <code data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">n</code> seats that are numbered from <code data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">1</code> to <code data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">n</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">設計一個系統，用於管理編號為的 <code data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">n</code> <code data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">1</code> <code data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">n</code> 座位的預訂狀態。</font></font></font></p>

<p>Implement the <code>SeatManager</code> class:</p>

<ul>
	<li data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1"><code data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">SeatManager(int n)</code> Initializes a <code data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">SeatManager</code> object that will manage <code data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">n</code> seats numbered from <code data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">1</code> to <code data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">n</code>. All seats are initially available.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"> <code data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">SeatManager(int n)</code> 初始化一個 <code data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">SeatManager</code> 物件，該物件將管理 <code data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">n</code> 編號為 的 <code data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">1</code> <code data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">n</code> 席位。所有座位最初都有空位。</font></font></font></li>
	<li data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1"><code data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">int reserve()</code> Fetches the <strong data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">smallest-numbered</strong> unreserved seat, reserves it, and returns its number.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"> <code data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">int reserve()</code> 獲取編號最小的未保留席位，保留該席位，並返回其編號。</font></font></font></li>
	<li data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1"><code data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">void unreserve(int seatNumber)</code> Unreserves the seat with the given <code data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">seatNumber</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"> <code data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">void unreserve(int seatNumber)</code> 取消保留給定 <code data-immersive-translate-effect="1" data-immersive_translate_walked="1c248faa-0482-425d-bb78-35f23e72e9d1">seatNumber</code> 的席位。</font></font></font></li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input</strong>
["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]
<strong>Output</strong>
[null, 1, 2, null, 2, 3, 4, 5, null]

<strong>Explanation</strong>
SeatManager seatManager = new SeatManager(5); // Initializes a SeatManager with 5 seats.
seatManager.reserve();    // All seats are available, so return the lowest numbered seat, which is 1.
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.unreserve(2); // Unreserve seat 2, so now the available seats are [2,3,4,5].
seatManager.reserve();    // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
seatManager.reserve();    // The available seats are [3,4,5], so return the lowest of them, which is 3.
seatManager.reserve();    // The available seats are [4,5], so return the lowest of them, which is 4.
seatManager.reserve();    // The only available seat is seat 5, so return 5.
seatManager.unreserve(5); // Unreserve seat 5, so now the available seats are [5].
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>1 &lt;= seatNumber &lt;= n</code></li>
	<li>For each call to <code>reserve</code>, it is guaranteed that there will be at least one unreserved seat.</li>
	<li>For each call to <code>unreserve</code>, it is guaranteed that <code>seatNumber</code> will be reserved.</li>
	<li>At most <code>10<sup>5</sup></code> calls <strong>in total</strong> will be made to <code>reserve</code> and <code>unreserve</code>.</li>
</ul>
</div>