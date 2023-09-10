<h2><a href="https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/">1359. Count All Valid Pickup and Delivery Options</a></h2><h3>Hard</h3><hr><div><p data-immersive-translate-effect="1" data-immersive_translate_walked="455ba33f-f9ff-47c6-85d0-5e3f2922e8e5">Given <code data-immersive-translate-effect="1" data-immersive_translate_walked="455ba33f-f9ff-47c6-85d0-5e3f2922e8e5">n</code> orders, each order consist in pickup and delivery services.&nbsp;<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">給定 <code data-immersive-translate-effect="1" data-immersive_translate_walked="455ba33f-f9ff-47c6-85d0-5e3f2922e8e5">n</code> 訂單，每個訂單都包括取貨和送貨服務。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="455ba33f-f9ff-47c6-85d0-5e3f2922e8e5">Count all valid pickup/delivery possible sequences such that delivery(i) is always after of&nbsp;pickup(i).&nbsp;<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">計算所有有效的取件/交貨可能序列，以便交貨 （i） 始終在取件 （i） 之後。</font></font></font></p>

<p data-immersive-translate-effect="1" data-immersive_translate_walked="455ba33f-f9ff-47c6-85d0-5e3f2922e8e5">Since the answer&nbsp;may be too large,&nbsp;return it modulo&nbsp;10^9 + 7.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1">由於答案可能太大，因此返回模 10^9 + 7。</font></font></font></p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> n = 1
<strong>Output:</strong> 1
<strong>Explanation:</strong> Unique order (P1, D1), Delivery 1 always is after of Pickup 1.
</pre>

<p><strong class="example">Example 2:</strong></p>

<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> 6
<strong>Explanation:</strong> All possible orders: 
(P1,P2,D1,D2), (P1,P2,D2,D1), (P1,D1,P2,D2), (P2,P1,D1,D2), (P2,P1,D2,D1) and (P2,D2,P1,D1).
This is an invalid order (P1,D2,P2,D1) because Pickup 2 is after of Delivery 2.
</pre>

<p><strong class="example">Example 3:</strong></p>

<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> 90
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 500</code></li>
</ul>
</div>