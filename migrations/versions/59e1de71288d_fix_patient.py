"""fix patient

Revision ID: 59e1de71288d
Revises: bfd58a42d96d
Create Date: 2022-04-22 14:20:26.837199

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '59e1de71288d'
down_revision = 'bfd58a42d96d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('patients', sa.Column('responsible_guardian', sa.String(), nullable=True))
    op.add_column('patients', sa.Column('responsible_contact', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('patients', 'responsible_contact')
    op.drop_column('patients', 'responsible_guardian')
    # ### end Alembic commands ###