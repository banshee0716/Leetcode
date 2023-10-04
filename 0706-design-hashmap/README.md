<h2><a href="https://leetcode.com/problems/design-hashmap/">706. Design HashMap</a></h2><h3>Easy</h3><hr><div><p>Design a HashMap without using any built-in hash table libraries.</p>

<p>Implement the <code>MyHashMap</code> class:</p>

<ul>
	<li data-immersive-translate-effect="1" data-immersive_translate_walked="a057532a-18e9-4f8f-91dc-50652477368f"><code data-immersive-translate-effect="1" data-immersive_translate_walked="a057532a-18e9-4f8f-91dc-50652477368f">MyHashMap()</code> initializes the object with an empty map.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"> <code data-immersive-translate-effect="1" data-immersive_translate_walked="a057532a-18e9-4f8f-91dc-50652477368f">MyHashMap()</code> 使用空映射初始化物件。</font></font></font></li>
	<li data-immersive-translate-effect="1" data-immersive_translate_walked="a057532a-18e9-4f8f-91dc-50652477368f"><code data-immersive-translate-effect="1" data-immersive_translate_walked="a057532a-18e9-4f8f-91dc-50652477368f">void put(int key, int value)</code> inserts a <code data-immersive-translate-effect="1" data-immersive_translate_walked="a057532a-18e9-4f8f-91dc-50652477368f">(key, value)</code> pair into the HashMap. If the <code data-immersive-translate-effect="1" data-immersive_translate_walked="a057532a-18e9-4f8f-91dc-50652477368f">key</code> already exists in the map, update the corresponding <code data-immersive-translate-effect="1" data-immersive_translate_walked="a057532a-18e9-4f8f-91dc-50652477368f">value</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"> <code data-immersive-translate-effect="1" data-immersive_translate_walked="a057532a-18e9-4f8f-91dc-50652477368f">void put(int key, int value)</code> 將一 <code data-immersive-translate-effect="1" data-immersive_translate_walked="a057532a-18e9-4f8f-91dc-50652477368f">(key, value)</code> 對插入到哈希映射中。如果映射中已存在 ， <code data-immersive-translate-effect="1" data-immersive_translate_walked="a057532a-18e9-4f8f-91dc-50652477368f">key</code> 請更新相應的 <code data-immersive-translate-effect="1" data-immersive_translate_walked="a057532a-18e9-4f8f-91dc-50652477368f">value</code> .</font></font></font></li>
	<li data-immersive-translate-effect="1" data-immersive_translate_walked="a057532a-18e9-4f8f-91dc-50652477368f"><code data-immersive-translate-effect="1" data-immersive_translate_walked="a057532a-18e9-4f8f-91dc-50652477368f">int get(int key)</code> returns the <code data-immersive-translate-effect="1" data-immersive_translate_walked="a057532a-18e9-4f8f-91dc-50652477368f">value</code> to which the specified <code data-immersive-translate-effect="1" data-immersive_translate_walked="a057532a-18e9-4f8f-91dc-50652477368f">key</code> is mapped, or <code data-immersive-translate-effect="1" data-immersive_translate_walked="a057532a-18e9-4f8f-91dc-50652477368f">-1</code> if this map contains no mapping for the <code data-immersive-translate-effect="1" data-immersive_translate_walked="a057532a-18e9-4f8f-91dc-50652477368f">key</code>.<font class="notranslate immersive-translate-target-wrapper" lang="zh-TW" data-immersive-translate-translation-element-mark="1"><br><font class="notranslate immersive-translate-target-translation-theme-none immersive-translate-target-translation-block-wrapper-theme-none immersive-translate-target-translation-block-wrapper" data-immersive-translate-translation-element-mark="1"><font class="notranslate immersive-translate-target-inner immersive-translate-target-translation-theme-none-inner" data-immersive-translate-translation-element-mark="1"> <code data-immersive-translate-effect="1" data-immersive_translate_walked="a057532a-18e9-4f8f-91dc-50652477368f">int get(int key)</code> 返回指定 <code data-immersive-translate-effect="1" data-immersive_translate_walked="a057532a-18e9-4f8f-91dc-50652477368f">key</code> 映射到的 ， <code data-immersive-translate-effect="1" data-immersive_translate_walked="a057532a-18e9-4f8f-91dc-50652477368f">value</code> 或者 <code data-immersive-translate-effect="1" data-immersive_translate_walked="a057532a-18e9-4f8f-91dc-50652477368f">-1</code> 如果此映射不包含的 <code data-immersive-translate-effect="1" data-immersive_translate_walked="a057532a-18e9-4f8f-91dc-50652477368f">key</code> 映射。</font></font></font></li>
	<li><code>void remove(key)</code> removes the <code>key</code> and its corresponding <code>value</code> if the map contains the mapping for the <code>key</code>.</li>
</ul>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input</strong>
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
<strong>Output</strong>
[null, null, null, 1, -1, null, 1, null, -1]

<strong>Explanation</strong>
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= key, value &lt;= 10<sup>6</sup></code></li>
	<li>At most <code>10<sup>4</sup></code> calls will be made to <code>put</code>, <code>get</code>, and <code>remove</code>.</li>
</ul>
</div>