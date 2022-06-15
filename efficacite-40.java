package convertisseur;

public class solutionCategorie2 {

	public static String convertirEfficace(String message) {

		if(message.contains(" ")) {
			StringBuilder nvMess = new StringBuilder(message);

			int index = nvMess.indexOf(" ");
			int index2 = 0;
			while(index!=-1) {
				index2 = nvMess.indexOf(" ", index+1);

				if(index2==index+1) {
					while(index2==index+1) {
						index=index2;
						index2 = nvMess.indexOf(" ", index+1);
					}
					if(index2==-1) {
						return nvMess.toString();
					} else {
						index=index2;
					}
				} 
				if(index!=-1) {
					nvMess.deleteCharAt(index);
				}
				index = nvMess.indexOf(" ", index+1);
			}
			return nvMess.toString();
		}
		return message;
	}
}
