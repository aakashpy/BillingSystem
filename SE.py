<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Form</class>
 <widget class="QWidget" name="Form">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1034</width>
    <height>686</height>
   </rect>
  </property>
  <property name="sizePolicy">
   <sizepolicy hsizetype="Fixed" vsizetype="Fixed">
    <horstretch>0</horstretch>
    <verstretch>0</verstretch>
   </sizepolicy>
  </property>
  <property name="minimumSize">
   <size>
    <width>1034</width>
    <height>686</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>1034</width>
    <height>686</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Form</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(172, 172, 172);</string>
  </property>
  <widget class="QWidget" name="widget" native="true">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>130</y>
     <width>381</width>
     <height>541</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(172, 172, 172);</string>
   </property>
   <widget class="QTableWidget" name="menucard2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>361</width>
      <height>521</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Courier</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
</string>
    </property>
    <property name="horizontalScrollBarPolicy">
     <enum>Qt::ScrollBarAlwaysOff</enum>
    </property>
    <property name="sizeAdjustPolicy">
     <enum>QAbstractScrollArea::AdjustToContentsOnFirstShow</enum>
    </property>
    <property name="alternatingRowColors">
     <bool>true</bool>
    </property>
    <property name="selectionMode">
     <enum>QAbstractItemView::SingleSelection</enum>
    </property>
    <property name="selectionBehavior">
     <enum>QAbstractItemView::SelectRows</enum>
    </property>
    <property name="showGrid">
     <bool>false</bool>
    </property>
    <attribute name="horizontalHeaderDefaultSectionSize">
     <number>230</number>
    </attribute>
    <attribute name="horizontalHeaderHighlightSections">
     <bool>false</bool>
    </attribute>
    <attribute name="horizontalHeaderStretchLastSection">
     <bool>true</bool>
    </attribute>
    <attribute name="verticalHeaderVisible">
     <bool>false</bool>
    </attribute>
    <column>
     <property name="text">
      <string>ITEMS</string>
     </property>
     <property name="font">
      <font>
       <family>Courier</family>
       <pointsize>12</pointsize>
      </font>
     </property>
    </column>
    <column>
     <property name="text">
      <string>PRICE</string>
     </property>
     <property name="font">
      <font>
       <family>Courier</family>
       <pointsize>12</pointsize>
      </font>
     </property>
     <property name="textAlignment">
      <set>AlignLeading|AlignVCenter</set>
     </property>
    </column>
   </widget>
   <widget class="QTableWidget" name="menucard1">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>361</width>
      <height>521</height>
     </rect>
    </property>
    <property name="maximumSize">
     <size>
      <width>3620</width>
      <height>5210</height>
     </size>
    </property>
    <property name="font">
     <font>
      <family>Courier</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);</string>
    </property>
    <property name="horizontalScrollBarPolicy">
     <enum>Qt::ScrollBarAlwaysOff</enum>
    </property>
    <property name="sizeAdjustPolicy">
     <enum>QAbstractScrollArea::AdjustToContents</enum>
    </property>
    <property name="alternatingRowColors">
     <bool>true</bool>
    </property>
    <property name="selectionMode">
     <enum>QAbstractItemView::SingleSelection</enum>
    </property>
    <property name="selectionBehavior">
     <enum>QAbstractItemView::SelectRows</enum>
    </property>
    <property name="showGrid">
     <bool>false</bool>
    </property>
    <attribute name="horizontalHeaderDefaultSectionSize">
     <number>230</number>
    </attribute>
    <attribute name="horizontalHeaderHighlightSections">
     <bool>false</bool>
    </attribute>
    <attribute name="horizontalHeaderStretchLastSection">
     <bool>true</bool>
    </attribute>
    <attribute name="verticalHeaderVisible">
     <bool>false</bool>
    </attribute>
    <column>
     <property name="text">
      <string>ITEMS</string>
     </property>
     <property name="font">
      <font>
       <family>Courier</family>
       <pointsize>12</pointsize>
      </font>
     </property>
    </column>
    <column>
     <property name="text">
      <string>PRICE</string>
     </property>
     <property name="font">
      <font>
       <family>Courier</family>
       <pointsize>12</pointsize>
      </font>
     </property>
     <property name="textAlignment">
      <set>AlignLeading|AlignVCenter</set>
     </property>
    </column>
   </widget>
  </widget>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>10</y>
     <width>1011</width>
     <height>51</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Courier</family>
     <pointsize>19</pointsize>
     <weight>75</weight>
     <bold>true</bold>
    </font>
   </property>
   <property name="text">
    <string>Zaika Family Restaurant</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
  </widget>
  <widget class="QWidget" name="widget_2" native="true">
   <property name="geometry">
    <rect>
     <x>400</x>
     <y>70</y>
     <width>621</width>
     <height>131</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(172, 172, 172);</string>
   </property>
   <widget class="QWidget" name="verticalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>601</width>
      <height>31</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout_2">
     <property name="sizeConstraint">
      <enum>QLayout::SetNoConstraint</enum>
     </property>
     <item>
      <widget class="QLabel" name="label_2">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="font">
        <font>
         <family>Courier</family>
         <pointsize>12</pointsize>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>Customer Name</string>
       </property>
       <property name="alignment">
        <set>Qt::AlignCenter</set>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLineEdit" name="name">
       <property name="minimumSize">
        <size>
         <width>0</width>
         <height>25</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Courier</family>
         <pointsize>12</pointsize>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(255, 255, 255);</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLabel" name="label_4">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="font">
        <font>
         <family>Courier</family>
         <pointsize>12</pointsize>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>Bill No.</string>
       </property>
       <property name="alignment">
        <set>Qt::AlignCenter</set>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLineEdit" name="billno">
       <property name="minimumSize">
        <size>
         <width>0</width>
         <height>25</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Courier</family>
         <pointsize>12</pointsize>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(255, 255, 255);</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="layoutWidget">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>50</y>
      <width>331</width>
      <height>31</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout_3">
     <property name="sizeConstraint">
      <enum>QLayout::SetNoConstraint</enum>
     </property>
     <item>
      <widget class="QLabel" name="label_3">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="maximumSize">
        <size>
         <width>111</width>
         <height>29</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Courier</family>
         <pointsize>12</pointsize>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>OrderItem</string>
       </property>
       <property name="alignment">
        <set>Qt::AlignCenter</set>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLineEdit" name="orderitem">
       <property name="minimumSize">
        <size>
         <width>0</width>
         <height>25</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>211</width>
         <height>20</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Courier</family>
         <pointsize>12</pointsize>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(255, 255, 255);</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="layoutWidget">
    <property name="geometry">
     <rect>
      <x>350</x>
      <y>50</y>
      <width>261</width>
      <height>31</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout_4">
     <property name="sizeConstraint">
      <enum>QLayout::SetNoConstraint</enum>
     </property>
     <item>
      <widget class="QLabel" name="label_5">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="font">
        <font>
         <family>Courier</family>
         <pointsize>12</pointsize>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>Quantity</string>
       </property>
       <property name="alignment">
        <set>Qt::AlignCenter</set>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QSpinBox" name="quantity">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Maximum" vsizetype="Minimum">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>60</width>
         <height>0</height>
        </size>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(255, 255, 255);</string>
       </property>
       <property name="alignment">
        <set>Qt::AlignCenter</set>
       </property>
       <property name="minimum">
        <number>1</number>
       </property>
       <property name="maximum">
        <number>10</number>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QWidget" name="verticalLayoutWidget_2">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>90</y>
      <width>601</width>
      <height>31</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout_5">
     <property name="sizeConstraint">
      <enum>QLayout::SetNoConstraint</enum>
     </property>
     <item>
      <widget class="QLabel" name="label_6">
       <property name="sizePolicy">
        <sizepolicy hsizetype="Minimum" vsizetype="Minimum">
         <horstretch>0</horstretch>
         <verstretch>0</verstretch>
        </sizepolicy>
       </property>
       <property name="minimumSize">
        <size>
         <width>114</width>
         <height>0</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>114</width>
         <height>16777215</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Courier</family>
         <pointsize>12</pointsize>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(255, 255, 255);</string>
       </property>
       <property name="text">
        <string>Price</string>
       </property>
       <property name="alignment">
        <set>Qt::AlignCenter</set>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QLineEdit" name="price">
       <property name="minimumSize">
        <size>
         <width>0</width>
         <height>25</height>
        </size>
       </property>
       <property name="maximumSize">
        <size>
         <width>211</width>
         <height>16777215</height>
        </size>
       </property>
       <property name="font">
        <font>
         <family>Courier</family>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">background-color: rgb(255, 255, 255);</string>
       </property>
      </widget>
     </item>
     <item>
      <widget class="QPushButton" name="add">
       <property name="font">
        <font>
         <family>Courier</family>
         <pointsize>12</pointsize>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">
background-color: rgb(0, 255, 0);</string>
       </property>
       <property name="text">
        <string>Add Item</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QWidget" name="widget_3" native="true">
   <property name="geometry">
    <rect>
     <x>400</x>
     <y>210</y>
     <width>621</width>
     <height>461</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(172, 172, 172);</string>
   </property>
   <widget class="QPushButton" name="Gbill">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>420</y>
      <width>141</width>
      <height>23</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Courier</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">
background-color: rgb(0, 255, 255);</string>
    </property>
    <property name="text">
     <string>Generate Bill</string>
    </property>
   </widget>
   <widget class="QPushButton" name="Sbill">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>420</y>
      <width>101</width>
      <height>23</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Courier</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 0);</string>
    </property>
    <property name="text">
     <string>Show Bill</string>
    </property>
   </widget>
   <widget class="QTextEdit" name="billtext">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>601</width>
      <height>401</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Courier</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="focusPolicy">
     <enum>Qt::WheelFocus</enum>
    </property>
    <property name="layoutDirection">
     <enum>Qt::LeftToRight</enum>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 255, 255);
</string>
    </property>
    <property name="locale">
     <locale language="English" country="UnitedStates"/>
    </property>
    <property name="inputMethodHints">
     <set>Qt::ImhMultiLine</set>
    </property>
    <property name="verticalScrollBarPolicy">
     <enum>Qt::ScrollBarAlwaysOn</enum>
    </property>
    <property name="html">
     <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'Courier'; font-size:12pt; font-weight:400; font-style:normal;&quot;&gt;
&lt;p align=&quot;center&quot; style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
    <property name="textInteractionFlags">
     <set>Qt::TextEditable|Qt::TextSelectableByMouse</set>
    </property>
   </widget>
   <widget class="QPushButton" name="clear">
    <property name="geometry">
     <rect>
      <x>540</x>
      <y>420</y>
      <width>75</width>
      <height>23</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Courier</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(255, 0, 0);
color: rgb(255, 255, 255);</string>
    </property>
    <property name="text">
     <string>Clear</string>
    </property>
   </widget>
  </widget>
  <widget class="QWidget" name="widget_4" native="true">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>70</y>
     <width>381</width>
     <height>41</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(172, 172, 172);</string>
   </property>
   <widget class="QPushButton" name="nvegbtn">
    <property name="geometry">
     <rect>
      <x>200</x>
      <y>10</y>
      <width>171</width>
      <height>26</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Courier</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">background-color: rgb(223, 0, 0);
color: rgb(255, 255, 255);</string>
    </property>
    <property name="text">
     <string>Non Veg</string>
    </property>
   </widget>
   <widget class="QPushButton" name="vegbtn">
    <property name="geometry">
     <rect>
      <x>9</x>
      <y>9</y>
      <width>171</width>
      <height>26</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Courier</family>
      <pointsize>12</pointsize>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">
background-color: rgb(0, 255, 0);</string>
    </property>
    <property name="text">
     <string>Veg</string>
    </property>
   </widget>
  </widget>
 </widget>
 <resources/>
 <connections/>
</ui>
