
import os
from math import pi as PI, cos
from time import sleep

# definitely not gonna be the cleanest code I've ever written
# this is more for proof of concept
frames = [
"""                                        
 .uu....,                      .....uu, 
 '4MMMMMbmmu,              .ummdMMMMMP' 
  ]MMMMMMMMMbu.,        ..udMMMMMMMMM[  
  `]MMMMMMMMMMML,      .]MMMMMMMMMMM7'  
   `]MMMMMMMMMMMbu,  .udMMMMMMMMMMM7'   
    ]MMMMMMMMMMMMM[  ]MMMMMMMMMMMMM[    
    `]MMMMMMMMMMMMb,.dMMMMMMMMMMMM7'    
     ]MMMMMMMMMMMMM[]MMMMMMMMMMMMM[     
     `^^^'****4MMMML]MMMMP****'^^^'     
      ...ummmmdMMMM7]MMMMbmmmmu..,      
      '4MMMMMMMMMMM[]MMMMMMMMMMMP'      
       ]MMMMMMMMMMP''4MMMMMMMMMM[       
       ]MMMMMMMMMM[  ]MMMMMMMMMM[       
       ]MMMMMMMMP''  `'4MMMMMMMM[       
       ]MMMMMMM7'      `]MMMMMMM[       
       `]MMMP'^'        `^'4MMM7'       
        '**''              `'**'        
                                        
                                        """,
"""                                        
 .uu....,                      .....uu, 
 `]MMMMMbmmu,              .ummdMMMMM7' 
  '4MMMMMMMMbmu,        .umdMMMMMMMMP'  
   ]MMMMMMMMMMMb,      .dMMMMMMMMMMM[   
   `]MMMMMMMMMMMbu,  .udMMMMMMMMMMM7'   
    '4MMMMMMMMMMMM[  ]MMMMMMMMMMMMP'    
     ]MMMMMMMMMMMMb,.dMMMMMMMMMMMM[     
     '4MMMMMMMMMMMM[]MMMMMMMMMMMMP'     
      `^^^'***4MMMML]MMMMP***'^^^'      
      ....ummmdMMMM7]MMMMbmmmu...,      
      `]MMMMMMMMMMM[]MMMMMMMMMMM7'      
       ]MMMMMMMMMMP''4MMMMMMMMMM[       
       ]MMMMMMMMMM[  ]MMMMMMMMMM[       
       ]MMMMMMMMP''  `'4MMMMMMMM[       
       `]MMMMMMP'      '4MMMMMM7'       
        ]MMMP*''        `'*4MMM[        
        '**''              `'**'        
                                        
                                        """,
"""                                        
  .uu....,                    .....uu,  
  '4MMMMMbmu,              .umdMMMMMP'  
   ]MMMMMMMMbmu,        .umdMMMMMMMM[   
   `]MMMMMMMMMMb,      .dMMMMMMMMMM7'   
    '4MMMMMMMMMMbu,  .udMMMMMMMMMMP'    
     ]MMMMMMMMMMMM[  ]MMMMMMMMMMMM[     
     '4MMMMMMMMMMMb,.dMMMMMMMMMMMP'     
      ]MMMMMMMMMMMM[]MMMMMMMMMMMM[      
      `^^^'****4MMML]MMMP****'^^^'      
       ...ummmmdMMM7]MMMbmmmmu..,       
       ]MMMMMMMMMMM[]MMMMMMMMMMM[       
       ]MMMMMMMMMMP''4MMMMMMMMMM[       
       `]MMMMMMMMM[  ]MMMMMMMMM7'       
        ]MMMMMMMP''  `'4MMMMMMM[        
        ]MMMMMMP'      '4MMMMMM[        
        ]MMMP*''        `'*4MMM[        
        '**''              `'**'        
                                        
                                        """,
"""                                        
   .u....,                    .....u,   
   '4MMMMbmu.,            ..umdMMMMP'   
    ]MMMMMMMMbu,        .udMMMMMMMM[    
    `]MMMMMMMMMbu,    .udMMMMMMMMM7'    
     ]MMMMMMMMMMML,  .]MMMMMMMMMMM[     
     `]MMMMMMMMMMML,.]MMMMMMMMMMM7'     
      ]MMMMMMMMMMMM[]MMMMMMMMMMMM[      
      `]MMMMMMMMMMM[]MMMMMMMMMMM7'      
       `^^'****4MMML]MMMP****'^^'       
        ..ummmmdMMM7]MMMbmmmmu.,        
        ]MMMMMMMMMM[]MMMMMMMMMM[        
        ]MMMMMMMMMM[]MMMMMMMMMM[        
        ]MMMMMMMMM7'`]MMMMMMMMM[        
        '4MMMMMMM7'  `]MMMMMMMP'        
         ]MMMMMP''    `'4MMMMM[         
         ]MMMP''        `'4MMM[         
         '*'^'            `^'*'         
                                        
                                        """,
"""                                        
    .u....,                  .....u,    
    `]MMMMbmu,            .umdMMMM7'    
     '4MMMMMMbm,        .mdMMMMMMP'     
      ]MMMMMMMMbu,    .udMMMMMMMM[      
      '4MMMMMMMMML,  .]MMMMMMMMMP'      
       ]MMMMMMMMMML,.]MMMMMMMMMM[       
       '4MMMMMMMMMM[]MMMMMMMMMMP'       
        ]MMMMMMMMMM[]MMMMMMMMMM[        
        `^^'***4MMML]MMMP***'^^'        
         ..ummmdMMM7]MMMbmmmu.,         
         ]MMMMMMMMM[]MMMMMMMMM[         
         ]MMMMMMMMM[]MMMMMMMMM[         
         ]MMMMMMMM7'`]MMMMMMMM[         
         '4MMMMMM7'  `]MMMMMMP'         
          ]MMMMP''    `'4MMMM[          
          ]MMP*'        '*4MM[          
          '*''            `'*'          
                                        
                                        """,
"""                                        
      .u...,                ....u,      
      '4MMMbmu,          .umdMMMP'      
       ]MMMMMMbu,      .udMMMMMM[       
       `]MMMMMMMb,    .dMMMMMMM7'       
        ]MMMMMMMMb,  .dMMMMMMMM[        
        '4MMMMMMMML,.]MMMMMMMMP'        
         ]MMMMMMMMM[]MMMMMMMMM[         
         ]MMMMMMMMM[]MMMMMMMMM[         
         `^^'***4MML]MMP***'^^'         
          ..ummmdMM7]MMbmmmu.,          
          ]MMMMMMMM[]MMMMMMMM[          
          ]MMMMMMMM[]MMMMMMMM[          
          `]MMMMMM7'`]MMMMMM7'          
           ]MMMMMP'  '4MMMMM[           
           ]MMMMP'    '4MMMM[           
           ]MMP''      `'4MM[           
           '*''          `'*'           
                                        
                                        """,
"""                                        
        .u...,            ....u,        
        '4MMMbu,        .udMMMP'        
         ]MMMMMb,      .dMMMMM[         
         '4MMMMMbu,  .udMMMMMP'         
          ]MMMMMMM[  ]MMMMMMM[          
          ]MMMMMMMb,.dMMMMMMM[          
          `]MMMMMMM[]MMMMMMM7'          
           ]MMMMMMM[]MMMMMMM[           
           `^'**4MML]MMP**'^'           
           ..ummdMM7]MMbmmu.,           
           `]MMMMMM[]MMMMMM7'           
            ]MMMMMM[]MMMMMM[            
            ]MMMMMP''4MMMMM[            
            ]MMMMM[  ]MMMMM[            
            ]MMMP''  `'4MMM[            
            ]MMP'      '4MM[            
            '*''        `'*'            
                                        
                                        """,
"""                                        
           ...,          ...,           
           ]MMbu,      .udMM[           
           ]MMMMb,    .dMMMM[           
           `]MMMMb,  .dMMMM7'           
            ]MMMMML,.]MMMMM[            
            ]MMMMMM[]MMMMMM[            
            '4MMMMM[]MMMMMP'            
             ]MMMMM[]MMMMM[             
             `^'*4ML]MP*'^'             
             ..umdM7]Mbmu.,             
             ]MMMMM[]MMMMM[             
             ]MMMMM[]MMMMM[             
             `]MMMM[]MMMM7'             
              ]MMM7'`]MMM[              
              ]MMP'  '4MM[              
              ]MP'    '4M[              
              '''      `''              
                                        
                                        """,
"""                                        
             ...,      ...,             
             ]MML,    .]MM[             
             `]MML,  .]MM7'             
              ]MMM[  ]MMM[              
              ]MMMb,.dMMM[              
              ]MMMM[]MMMM[              
              '4MMM[]MMMP'              
               ]MMM[]MMM[               
               `'*4L]P*''               
               .umd7]bmu,               
               ]MMM[]MMM[               
               ]MMM[]MMM[               
               ]MMM[]MMM[               
               ]MMP''4MM[               
               ]MM[  ]MM[               
               ]M7'  `]M[               
               `'      `'               
                                        
                                        """,
"""                                        
                .,    .,                
                ]b,  .d[                
                ]ML,.]M[                
                ]MM[]MM[                
                '4M[]MP'                
                 ]M[]M[                 
                 ]M[]M[                 
                 ]M[]M[                 
                 `'::''                 
                 .u[:u,                 
                 ]M[]M[                 
                 ]M[]M[                 
                 ]M[]M[                 
                 ]M[]M[                 
                 ]M[]M[                 
                 ]7'`][                 
                 ''  ''                 
                                        
                                        """,
"""                                        
                  ,  .                  
                  L,.]                  
                  ][]7                  
                   []                   
                   []                   
                   []                   
                   []                   
                   []                   
                   ::                   
                   [:                   
                   []                   
                   []                   
                   []                   
                   []                   
                   []                   
                   []                   
                   '`                   
                                        
                                        """,
"""                                        
                 .,  .,                 
                 ]L,.][                 
                 `][]7'                 
                  ][][                  
                  ][][                  
                  ][][                  
                  ][][                  
                  ][][                  
                  '::'                  
                  .[:,                  
                  ][][                  
                  ][][                  
                  ][][                  
                  ][][                  
                  ][][                  
                  ][][                  
                  `'`'                  
                                        
                                        """,
"""                                        
               ..,    ..,               
               ]ML,  .]M[               
               ]MM[  ]MM[               
               ]MML,.]MM[               
               ]MMM[]MMM[               
               '4MM[]MMP'               
                ]MM[]MM[                
                ]MM[]MM[                
                `'4L]P''                
                .ud7]bu,                
                ]MM[]MM[                
                ]MM[]MM[                
                ]MM[]MM[                
                ]MM[]MM[                
                ]M7'`]M[                
                ]M[  ]M[                
                `'    `'                
                                        
                                        """,
"""                                        
            ...,        ...,            
            ]MMb,      .dMM[            
            '4MMb,    .dMMP'            
             ]MMMb,  .dMMM[             
             ]MMMML,.]MMMM[             
             ]MMMMM[]MMMMM[             
             '4MMMM[]MMMMP'             
              ]MMMM[]MMMM[              
              `'*4ML]MP*''              
              .umdM7]Mbmu,              
              ]MMMM[]MMMM[              
              ]MMMM[]MMMM[              
              ]MMMM[]MMMM[              
              '4MM7'`]MMP'              
               ]MP'  '4M[               
               ]P'    '4[               
               ''      ''               
                                        
                                        """,
"""                                        
         .u..,            ...u,         
         `]MMbmu,      .umdMM7'         
          ]MMMMML,    .]MMMMM[          
          '4MMMMML,  .]MMMMMP'          
           ]MMMMMM[  ]MMMMMM[           
           ]MMMMMMb,.dMMMMMM[           
           '4MMMMMM[]MMMMMMP'           
            ]MMMMMM[]MMMMMM[            
            `^'**4ML]MP**'^'            
            ..ummdM7]Mbmmu.,            
            ]MMMMMM[]MMMMMM[            
            `]MMMMM[]MMMMM7'            
             ]MMMMP''4MMMM[             
             ]MMMM[  ]MMMM[             
             ]MMM7'  `]MMM[             
             ]MM7'    `]MM[             
             '*''      `'*'             
                                        
                                        """,
"""                                        
       .u...,              ....u,       
       '4MMMbmu,        .umdMMMP'       
        ]MMMMMML,      .]MMMMMM[        
        '4MMMMMMb,    .dMMMMMMP'        
         ]MMMMMMMb,  .dMMMMMMM[         
         ]MMMMMMMML,.]MMMMMMMM[         
         `]MMMMMMMM[]MMMMMMMM7'         
          ]MMMMMMMM[]MMMMMMMM[          
          `^^'**4MML]MMP**'^^'          
           ..ummdMM7]MMbmmu.,           
           ]MMMMMMM[]MMMMMMM[           
           ]MMMMMMM[]MMMMMMM[           
           ]MMMMMM7'`]MMMMMM[           
           ]MMMMMP'  '4MMMMM[           
           ]MMMMP'    '4MMMM[           
           `]MM7'      `]MM7'           
            '*''        `'*'            
                                        
                                        """,
"""                                        
     .uu...,                ....uu,     
     '4MMMMbmu,          .umdMMMMP'     
      ]MMMMMMMbu,      .udMMMMMMM[      
      `]MMMMMMMML,    .]MMMMMMMM7'      
       ]MMMMMMMMMb,  .dMMMMMMMMM[       
       `]MMMMMMMMML,.]MMMMMMMMM7'       
        ]MMMMMMMMMM[]MMMMMMMMMM[        
        '4MMMMMMMMM[]MMMMMMMMMP'        
         `^^'***4MML]MMP***'^^'         
         ...ummmdMM7]MMbmmmu..,         
         '4MMMMMMMM[]MMMMMMMMP'         
          ]MMMMMMMM[]MMMMMMMM[          
          ]MMMMMMM7'`]MMMMMMM[          
          ]MMMMMMP'  '4MMMMMM[          
          ]MMMMM7'    `]MMMMM[          
          ]MMMP''      `'4MMM[          
          '**''          `'**'          
                                        
                                        """,
"""                                        
    .uu...,                  ....uu,    
    ]MMMMMbmu,            .umdMMMMM[    
    `]MMMMMMMbu,        .udMMMMMMM7'    
     ]MMMMMMMMMbu,    .udMMMMMMMMM[     
     `]MMMMMMMMMML,  .]MMMMMMMMMM7'     
      '4MMMMMMMMMML,.]MMMMMMMMMMP'      
       ]MMMMMMMMMMM[]MMMMMMMMMMM[       
       ]MMMMMMMMMMM[]MMMMMMMMMMM[       
       `^^^'***4MMML]MMMP***'^^^'       
        ...ummmdMMM7]MMMbmmmu..,        
        ]MMMMMMMMMM[]MMMMMMMMMM[        
        `]MMMMMMMMM[]MMMMMMMMM7'        
         ]MMMMMMMM7'`]MMMMMMMM[         
         ]MMMMMMM7'  `]MMMMMMM[         
         ]MMMMMP''    `'4MMMMM[         
         ]MMMP''        `'4MMM[         
         '**''            `'**'         
                                        
                                        """,
"""                                        
  .uu....,                    .....uu,  
  `]MMMMMbmu.,            ..umdMMMMM7'  
   '4MMMMMMMMbu,        .udMMMMMMMMP'   
    ]MMMMMMMMMMb,      .dMMMMMMMMMM[    
    `]MMMMMMMMMMbu,  .udMMMMMMMMMM7'    
     '4MMMMMMMMMMM[  ]MMMMMMMMMMMP'     
      ]MMMMMMMMMMMb,.dMMMMMMMMMMM[      
      ]MMMMMMMMMMMM[]MMMMMMMMMMMM[      
      `^^^'****4MMML]MMMP****'^^^'      
       ...ummmmdMMM7]MMMbmmmmu..,       
       '4MMMMMMMMMM[]MMMMMMMMMMP'       
        ]MMMMMMMMMP''4MMMMMMMMM[        
        ]MMMMMMMMM[  ]MMMMMMMMM[        
        ]MMMMMMMP''  `'4MMMMMMM[        
        ]MMMMMMP'      '4MMMMMM[        
        ]MMMMP''        `'4MMMM[        
        '**''              `'**'        
                                        
                                        """,
"""                                        
 .uu.....,                    ......uu, 
 `]MMMMMMbmu,              .umdMMMMMM7' 
  `]MMMMMMMMbmu,        .umdMMMMMMMM7'  
   '4MMMMMMMMMMb,      .dMMMMMMMMMMP'   
    ]MMMMMMMMMMMbu,  .udMMMMMMMMMMM[    
    `]MMMMMMMMMMMM[  ]MMMMMMMMMMMM7'    
     ]MMMMMMMMMMMMb,.dMMMMMMMMMMMM[     
     `]MMMMMMMMMMMM[]MMMMMMMMMMMM7'     
      `^^^'****4MMML]MMMP****'^^^'      
       ...ummmmdMMM7]MMMbmmmmu..,       
       ]MMMMMMMMMMM[]MMMMMMMMMMM[       
       ]MMMMMMMMMMP''4MMMMMMMMMM[       
       ]MMMMMMMMMM[  ]MMMMMMMMMM[       
       `]MMMMMMMP''  `'4MMMMMMM7'       
        ]MMMMMMP'      '4MMMMMM[        
        ]MMMP*''        `'*4MMM[        
        '**''              `'**'        
                                        
                                        """,
"""                                        
 .uu....,                      .....uu, 
 '4MMMMMbmmu,              .ummdMMMMMP' 
  '4MMMMMMMMbu.,        ..udMMMMMMMMP'  
   ]MMMMMMMMMMML,      .]MMMMMMMMMMM[   
   `]MMMMMMMMMMMbu,  .udMMMMMMMMMMM7'   
    ]MMMMMMMMMMMMM[  ]MMMMMMMMMMMMM[    
    `]MMMMMMMMMMMMb,.dMMMMMMMMMMMM7'    
     ]MMMMMMMMMMMMM[]MMMMMMMMMMMMM[     
     `^^^'****4MMMML]MMMMP****'^^^'     
      ...ummmmdMMMM7]MMMMbmmmmu..,      
      '4MMMMMMMMMMM[]MMMMMMMMMMMP'      
       ]MMMMMMMMMMP''4MMMMMMMMMM[       
       ]MMMMMMMMMM[  ]MMMMMMMMMM[       
       ]MMMMMMMMP''  `'4MMMMMMMM[       
       ]MMMMMMM7'      `]MMMMMMM[       
       `]MMMP'^'        `^'4MMM7'       
        '**''              `'**'        
                                        
                                        """,
"""                                        
 .uu....,                      .....uu, 
 '4MMMMMbmmu,              .ummdMMMMMP' 
  '4MMMMMMMMbu.,        ..udMMMMMMMMP'  
   ]MMMMMMMMMMML,      .]MMMMMMMMMMM[   
   `]MMMMMMMMMMMbu,  .udMMMMMMMMMMM7'   
    ]MMMMMMMMMMMMM[  ]MMMMMMMMMMMMM[    
    `]MMMMMMMMMMMMb,.dMMMMMMMMMMMM7'    
     ]MMMMMMMMMMMMM[]MMMMMMMMMMMMM[     
     `^^^'****4MMMML]MMMMP****'^^^'     
      ...ummmmdMMMM7]MMMMbmmmmu..,      
      '4MMMMMMMMMMM[]MMMMMMMMMMMP'      
       ]MMMMMMMMMMP''4MMMMMMMMMM[       
       ]MMMMMMMMMM[  ]MMMMMMMMMM[       
       ]MMMMMMMMP''  `'4MMMMMMMM[       
       ]MMMMMMM7'      `]MMMMMMM[       
       `]MMMP'^'        `^'4MMM7'       
        '**''              `'**'        
                                        
                                        """,
"""                                        
 .uu.....,                    ......uu, 
 `]MMMMMMbmu,              .umdMMMMMM7' 
  `]MMMMMMMMbmu,        .umdMMMMMMMM7'  
   '4MMMMMMMMMMb,      .dMMMMMMMMMMP'   
    ]MMMMMMMMMMMbu,  .udMMMMMMMMMMM[    
    `]MMMMMMMMMMMM[  ]MMMMMMMMMMMM7'    
     ]MMMMMMMMMMMMb,.dMMMMMMMMMMMM[     
     `]MMMMMMMMMMMM[]MMMMMMMMMMMM7'     
      `^^^'****4MMML]MMMP****'^^^'      
       ...ummmmdMMM7]MMMbmmmmu..,       
       ]MMMMMMMMMMM[]MMMMMMMMMMM[       
       ]MMMMMMMMMMP''4MMMMMMMMMM[       
       ]MMMMMMMMMM[  ]MMMMMMMMMM[       
       `]MMMMMMMP''  `'4MMMMMMM7'       
        ]MMMMMMP'      '4MMMMMM[        
        ]MMMP*''        `'*4MMM[        
        '**''              `'**'        
                                        
                                        """,
"""                                        
  .uu....,                    .....uu,  
  `]MMMMMbmu.,            ..umdMMMMM7'  
   '4MMMMMMMMbu,        .udMMMMMMMMP'   
    ]MMMMMMMMMMb,      .dMMMMMMMMMM[    
    `]MMMMMMMMMMbu,  .udMMMMMMMMMM7'    
     '4MMMMMMMMMMM[  ]MMMMMMMMMMMP'     
      ]MMMMMMMMMMMb,.dMMMMMMMMMMM[      
      ]MMMMMMMMMMMM[]MMMMMMMMMMMM[      
      `^^^'****4MMML]MMMP****'^^^'      
       ...ummmmdMMM7]MMMbmmmmu..,       
       '4MMMMMMMMMM[]MMMMMMMMMMP'       
        ]MMMMMMMMMP''4MMMMMMMMM[        
        ]MMMMMMMMM[  ]MMMMMMMMM[        
        ]MMMMMMMP''  `'4MMMMMMM[        
        ]MMMMMMP'      '4MMMMMM[        
        ]MMMMP''        `'4MMMM[        
        '**''              `'**'        
                                        
                                        """,
"""                                        
    .u....,                  .....u,    
    ]MMMMMbmu,            .umdMMMMM[    
    `]MMMMMMMbu,        .udMMMMMMM7'    
     ]MMMMMMMMMbu,    .udMMMMMMMMM[     
     `]MMMMMMMMMML,  .]MMMMMMMMMM7'     
      '4MMMMMMMMMML,.]MMMMMMMMMMP'      
       ]MMMMMMMMMMM[]MMMMMMMMMMM[       
       ]MMMMMMMMMMM[]MMMMMMMMMMM[       
       `^^^'***4MMML]MMMP***'^^^'       
        ...ummmdMMM7]MMMbmmmu..,        
        ]MMMMMMMMMM[]MMMMMMMMMM[        
        `]MMMMMMMMM[]MMMMMMMMM7'        
         ]MMMMMMMM7'`]MMMMMMMM[         
         ]MMMMMMM7'  `]MMMMMMM[         
         ]MMMMMP''    `'4MMMMM[         
         ]MMMP''        `'4MMM[         
         '**''            `'**'         
                                        
                                        """,
"""                                        
     .u....,                .....u,     
     '4MMMMbmu,          .umdMMMMP'     
      ]MMMMMMMbu,      .udMMMMMMM[      
      `]MMMMMMMML,    .]MMMMMMMM7'      
       ]MMMMMMMMMb,  .dMMMMMMMMM[       
       `]MMMMMMMMML,.]MMMMMMMMM7'       
        ]MMMMMMMMMM[]MMMMMMMMMM[        
        '4MMMMMMMMM[]MMMMMMMMMP'        
         `^^'***4MML]MMP***'^^'         
         ...ummmdMM7]MMbmmmu..,         
         '4MMMMMMMM[]MMMMMMMMP'         
          ]MMMMMMMM[]MMMMMMMM[          
          ]MMMMMMM7'`]MMMMMMM[          
          ]MMMMMMP'  '4MMMMMM[          
          ]MMMMM7'    `]MMMMM[          
          ]MMMP''      `'4MMM[          
          '**''          `'**'          
                                        
                                        """,
"""                                        
       .u...,              ....u,       
       '4MMMbmu,        .umdMMMP'       
        ]MMMMMML,      .]MMMMMM[        
        '4MMMMMMb,    .dMMMMMMP'        
         ]MMMMMMMb,  .dMMMMMMM[         
         ]MMMMMMMML,.]MMMMMMMM[         
         `]MMMMMMMM[]MMMMMMMM7'         
          ]MMMMMMMM[]MMMMMMMM[          
          `^^'**4MML]MMP**'^^'          
           ..ummdMM7]MMbmmu.,           
           ]MMMMMMM[]MMMMMMM[           
           ]MMMMMMM[]MMMMMMM[           
           ]MMMMMM7'`]MMMMMM[           
           ]MMMMMP'  '4MMMMM[           
           ]MMMMP'    '4MMMM[           
           `]MM7'      `]MM7'           
            '*''        `'*'            
                                        
                                        """,
"""                                        
         .u..,            ...u,         
         `]MMbmu,      .umdMM7'         
          ]MMMMML,    .]MMMMM[          
          '4MMMMML,  .]MMMMMP'          
           ]MMMMMM[  ]MMMMMM[           
           ]MMMMMMb,.dMMMMMM[           
           '4MMMMMM[]MMMMMMP'           
            ]MMMMMM[]MMMMMM[            
            `^'**4ML]MP**'^'            
            ..ummdM7]Mbmmu.,            
            ]MMMMMM[]MMMMMM[            
            `]MMMMM[]MMMMM7'            
             ]MMMMP''4MMMM[             
             ]MMMM[  ]MMMM[             
             ]MMM7'  `]MMM[             
             ]MM7'    `]MM[             
             '*''      `'*'             
                                        
                                        """,
"""                                        
            ...,        ...,            
            ]MMb,      .dMM[            
            '4MMb,    .dMMP'            
             ]MMMb,  .dMMM[             
             ]MMMML,.]MMMM[             
             ]MMMMM[]MMMMM[             
             '4MMMM[]MMMMP'             
              ]MMMM[]MMMM[              
              `'*4ML]MP*''              
              .umdM7]Mbmu,              
              ]MMMM[]MMMM[              
              ]MMMM[]MMMM[              
              ]MMMM[]MMMM[              
              '4MM7'`]MMP'              
               ]MP'  '4M[               
               ]P'    '4[               
               ''      ''               
                                        
                                        """,
"""                                        
               ..,    ..,               
               ]ML,  .]M[               
               ]MM[  ]MM[               
               ]MML,.]MM[               
               ]MMM[]MMM[               
               '4MM[]MMP'               
                ]MM[]MM[                
                ]MM[]MM[                
                `'4L]P''                
                .ud7]bu,                
                ]MM[]MM[                
                ]MM[]MM[                
                ]MM[]MM[                
                ]MM[]MM[                
                ]M7'`]M[                
                ]M[  ]M[                
                ''    ''                
                                        
                                        """,
"""                                        
                 .,  .,                 
                 ]L,.][                 
                 `][]7'                 
                  ][][                  
                  ][][                  
                  ][][                  
                  ][][                  
                  ][][                  
                  '::'                  
                  .[:,                  
                  ][][                  
                  ][][                  
                  ][][                  
                  ][][                  
                  ][][                  
                  ][][                  
                  `'`'                  
                                        
                                        """,
"""                                        
                  ,  .                  
                  L,.]                  
                  ][]7                  
                   []                   
                   []                   
                   []                   
                   []                   
                   []                   
                   ::                   
                   [:                   
                   []                   
                   []                   
                   []                   
                   []                   
                   []                   
                   []                   
                   '`                   
                                        
                                        """,
"""                                        
                .,    .,                
                ]b,  .d[                
                ]ML,.]M[                
                ]MM[]MM[                
                '4M[]MP'                
                 ]M[]M[                 
                 ]M[]M[                 
                 ]M[]M[                 
                 `'::''                 
                 .u[:u,                 
                 ]M[]M[                 
                 ]M[]M[                 
                 ]M[]M[                 
                 ]M[]M[                 
                 ]M[]M[                 
                 ]7'`][                 
                 ''  ''                 
                                        
                                        """,
"""                                        
             ...,      ...,             
             ]MML,    .]MM[             
             `]MML,  .]MM7'             
              ]MMM[  ]MMM[              
              ]MMMb,.dMMM[              
              ]MMMM[]MMMM[              
              '4MMM[]MMMP'              
               ]MMM[]MMM[               
               `'*4L]P*''               
               .umd7]bmu,               
               ]MMM[]MMM[               
               ]MMM[]MMM[               
               ]MMM[]MMM[               
               ]MMP''4MM[               
               ]MM[  ]MM[               
               ]M7'  `]M[               
               ''      ''               
                                        
                                        """,
"""                                        
           ...,          ...,           
           ]MMbu,      .udMM[           
           ]MMMMb,    .dMMMM[           
           `]MMMMb,  .dMMMM7'           
            ]MMMMML,.]MMMMM[            
            ]MMMMMM[]MMMMMM[            
            '4MMMMM[]MMMMMP'            
             ]MMMMM[]MMMMM[             
             `^'*4ML]MP*'^'             
             ..umdM7]Mbmu.,             
             ]MMMMM[]MMMMM[             
             ]MMMMM[]MMMMM[             
             `]MMMM[]MMMM7'             
              ]MMM7'`]MMM[              
              ]MMP'  '4MM[              
              ]MP'    '4M[              
              '''      `''              
                                        
                                        """,
"""                                        
        .u...,            ....u,        
        '4MMMbu,        .udMMMP'        
         ]MMMMMb,      .dMMMMM[         
         '4MMMMMbu,  .udMMMMMP'         
          ]MMMMMMM[  ]MMMMMMM[          
          ]MMMMMMMb,.dMMMMMMM[          
          `]MMMMMMM[]MMMMMMM7'          
           ]MMMMMMM[]MMMMMMM[           
           `^'**4MML]MMP**'^'           
           ..ummdMM7]MMbmmu.,           
           `]MMMMMM[]MMMMMM7'           
            ]MMMMMM[]MMMMMM[            
            ]MMMMMP''4MMMMM[            
            ]MMMMM[  ]MMMMM[            
            ]MMMP''  `'4MMM[            
            ]MMP'      '4MM[            
            '*''        `'*'            
                                        
                                        """,
"""                                        
      .u...,                ....u,      
      '4MMMbmu,          .umdMMMP'      
       ]MMMMMMbu,      .udMMMMMM[       
       `]MMMMMMMb,    .dMMMMMMM7'       
        ]MMMMMMMMb,  .dMMMMMMMM[        
        '4MMMMMMMML,.]MMMMMMMMP'        
         ]MMMMMMMMM[]MMMMMMMMM[         
         ]MMMMMMMMM[]MMMMMMMMM[         
         `^^'***4MML]MMP***'^^'         
          ..ummmdMM7]MMbmmmu.,          
          ]MMMMMMMM[]MMMMMMMM[          
          ]MMMMMMMM[]MMMMMMMM[          
          `]MMMMMM7'`]MMMMMM7'          
           ]MMMMMP'  '4MMMMM[           
           ]MMMMP'    '4MMMM[           
           ]MMP''      `'4MM[           
           '*''          `'*'           
                                        
                                        """,
"""                                        
    .uu...,                  ....uu,    
    `]MMMMbmu,            .umdMMMM7'    
     '4MMMMMMbm,        .mdMMMMMMP'     
      ]MMMMMMMMbu,    .udMMMMMMMM[      
      '4MMMMMMMMML,  .]MMMMMMMMMP'      
       ]MMMMMMMMMML,.]MMMMMMMMMM[       
       '4MMMMMMMMMM[]MMMMMMMMMMP'       
        ]MMMMMMMMMM[]MMMMMMMMMM[        
        `^^'***4MMML]MMMP***'^^'        
         ..ummmdMMM7]MMMbmmmu.,         
         ]MMMMMMMMM[]MMMMMMMMM[         
         ]MMMMMMMMM[]MMMMMMMMM[         
         ]MMMMMMMM7'`]MMMMMMMM[         
         '4MMMMMM7'  `]MMMMMMP'         
          ]MMMMP''    `'4MMMM[          
          ]MMP*'        '*4MM[          
          '*''            `'*'          
                                        
                                        """,
"""                                        
   .uu...,                    ....uu,   
   '4MMMMbmu.,            ..umdMMMMP'   
    ]MMMMMMMMbu,        .udMMMMMMMM[    
    `]MMMMMMMMMbu,    .udMMMMMMMMM7'    
     ]MMMMMMMMMMML,  .]MMMMMMMMMMM[     
     `]MMMMMMMMMMML,.]MMMMMMMMMMM7'     
      ]MMMMMMMMMMMM[]MMMMMMMMMMMM[      
      `]MMMMMMMMMMM[]MMMMMMMMMMM7'      
       `^^'****4MMML]MMMP****'^^'       
        ..ummmmdMMM7]MMMbmmmmu.,        
        ]MMMMMMMMMM[]MMMMMMMMMM[        
        ]MMMMMMMMMM[]MMMMMMMMMM[        
        ]MMMMMMMMM7'`]MMMMMMMMM[        
        '4MMMMMMM7'  `]MMMMMMMP'        
         ]MMMMMP''    `'4MMMMM[         
         ]MMMP''        `'4MMM[         
         '*'^'            `^'*'         
                                        
                                        """,
"""                                        
  .uu....,                    .....uu,  
  '4MMMMMbmu,              .umdMMMMMP'  
   ]MMMMMMMMbmu,        .umdMMMMMMMM[   
   `]MMMMMMMMMMb,      .dMMMMMMMMMM7'   
    '4MMMMMMMMMMbu,  .udMMMMMMMMMMP'    
     ]MMMMMMMMMMMM[  ]MMMMMMMMMMMM[     
     '4MMMMMMMMMMMb,.dMMMMMMMMMMMP'     
      ]MMMMMMMMMMMM[]MMMMMMMMMMMM[      
      `^^^'****4MMML]MMMP****'^^^'      
       ...ummmmdMMM7]MMMbmmmmu..,       
       ]MMMMMMMMMMM[]MMMMMMMMMMM[       
       ]MMMMMMMMMMP''4MMMMMMMMMM[       
       `]MMMMMMMMM[  ]MMMMMMMMM7'       
        ]MMMMMMMP''  `'4MMMMMMM[        
        ]MMMMMMP'      '4MMMMMM[        
        ]MMMP*''        `'*4MMM[        
        '**''              `'**'        
                                        
                                        """,
"""                                        
 .uu....,                      .....uu, 
 `]MMMMMbmmu,              .ummdMMMMM7' 
  '4MMMMMMMMbmu,        .umdMMMMMMMMP'  
   ]MMMMMMMMMMMb,      .dMMMMMMMMMMM[   
   `]MMMMMMMMMMMbu,  .udMMMMMMMMMMM7'   
    '4MMMMMMMMMMMM[  ]MMMMMMMMMMMMP'    
     ]MMMMMMMMMMMMb,.dMMMMMMMMMMMM[     
     '4MMMMMMMMMMMM[]MMMMMMMMMMMMP'     
      `^^^'***4MMMML]MMMMP***'^^^'      
      ....ummmdMMMM7]MMMMbmmmu...,      
      `]MMMMMMMMMMM[]MMMMMMMMMMM7'      
       ]MMMMMMMMMMP''4MMMMMMMMMM[       
       ]MMMMMMMMMM[  ]MMMMMMMMMM[       
       ]MMMMMMMMP''  `'4MMMMMMMM[       
       `]MMMMMMP'      '4MMMMMM7'       
        ]MMMP*''        `'*4MMM[        
        '**''              `'**'        
                                        
"""
]

def animate(n):
    """
    run the rotating butterfly animation for n frames
    runs at 12 fps
    """

    num_frames = len(frames)

    min_width = 40
    min_height = 20

    width, height = os.get_terminal_size()

    if width < min_width or height < min_height:
        print(f"ERROR: terminal screen is too small. Minimum {min_width}x{min_height}")
        exit(1)

    height_offset = (height - min_height) // 2
    height_padding = "\n" * height_offset

    width_offset = (width - min_width) // 2
    width_padding = " " * width_offset

    for i in range(num_frames):
        frames[i] = frames[i].replace("\n", "\n" + width_padding)
        frames[i] = height_padding + frames[i]

    dt = 1 / 12

    index = 0
    for _ in range(n):
        os.system("clear")
        print(frames[index])
        index = (index + 1) % num_frames
        sleep(dt)

def main():
    animate(10000)

if __name__ == "__main__":
    main()