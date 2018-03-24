/*
claass Node 
       int data;
       Node left;
       Node right;
   */
   void levelOrder(Node root) {
       if(root==null)
           return;
       java.util.List<Node> l=new java.util.ArrayList<Node>();
       java.util.List<Node> newList;
       System.out.print(root.data+" ");
       if(root.left!=null)
            l.add(root.left);
       if(root.right!=null)
            l.add(root.right);
       
       while(!l.isEmpty()){
           newList=new java.util.ArrayList<Node>();
           for(Node n:l){
                System.out.print(n.data+" ");
               if(n.left!=null) 
                    newList.add(n.left);
               if(n.right!=null)
                    newList.add(n.right);
               
           }
           l=newList;
       }
       
    }
